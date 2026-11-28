"""
Rate limit handling utilities for GitHub API
"""
import time
import random
import os
from typing import Dict, Optional
import requests

class RateLimitHandler:
    def __init__(self):
        self.base_delay = 1
        self.max_retries = 3
        self.jitter_range = (1, 5)

    def get_headers(self) -> Dict[str, str]:
        """Get headers for GitHub API requests with authentication if available."""
        headers = {'Accept': 'application/vnd.github.v3+json'}
        github_token = os.getenv('GITHUB_TOKEN')
        if github_token:
            headers['Authorization'] = f'Bearer {github_token}'
        return headers

    def handle_rate_limit(self, response: requests.Response) -> Optional[int]:
        """
        Handle GitHub API rate limit response.
        
        Args:
            response: API response object
            
        Returns:
            Optional[int]: Wait time in seconds if rate limited, None otherwise
        """
        if response.status_code == 403 and 'rate limit exceeded' in response.text.lower():
            reset_time = int(response.headers.get('X-RateLimit-Reset', 0))
            current_time = int(time.time())
            wait_time = max(reset_time - current_time, 0)
            
            if not os.getenv('GITHUB_TOKEN'):
                raise Exception(
                    "GitHub API rate limit exceeded. Please set GITHUB_TOKEN environment variable "
                    "to increase rate limit."
                )
            
            jitter = random.uniform(*self.jitter_range)
            return wait_time + jitter
        return None

    def get_exponential_backoff(self, retry_count: int) -> float:
        """Calculate exponential backoff with jitter."""
        delay = self.base_delay * (2 ** retry_count)
        jitter = random.uniform(0, 1)
        return delay + jitter

    def make_request(self, url: str, method: str = 'GET', **kwargs) -> requests.Response:
        """
        Make an API request with rate limit handling and retries.
        
        Args:
            url: API endpoint URL
            method: HTTP method
            **kwargs: Additional arguments for requests
            
        Returns:
            Response object
            
        Raises:
            Exception: If request fails after all retries
        """
        headers = self.get_headers()
        kwargs['headers'] = headers

        for retry_count in range(self.max_retries):
            try:
                response = requests.request(method, url, **kwargs)
                
                # Check for rate limit
                wait_time = self.handle_rate_limit(response)
                if wait_time:
                    print(f"Rate limit exceeded. Waiting {wait_time:.2f} seconds...")
                    time.sleep(wait_time)
                    continue
                
                if response.status_code == 200:
                    return response
                    
                if response.status_code != 200:
                    print(f"API Error! Status Code: {response.status_code}")
                    print(f"Response: {response.text}")
                    
            except requests.exceptions.RequestException as e:
                if retry_count == self.max_retries - 1:
                    raise Exception(f"Failed to make request after {self.max_retries} retries: {str(e)}")
                
                delay = self.get_exponential_backoff(retry_count)
                print(f"Request failed, retrying in {delay:.2f} seconds... (Attempt {retry_count + 1}/{self.max_retries})")
                time.sleep(delay)
        
        raise Exception(f"Failed to make request after {self.max_retries} retries") 