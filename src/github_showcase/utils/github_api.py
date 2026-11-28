"""
GitHub API utility for fetching repository data
"""
from typing import List, Dict
from ..config.settings import GITHUB_USERNAME, EXCLUDE_REPOS
from .rate_limit import RateLimitHandler

def get_all_repositories() -> List[Dict]:
    """
    Fetch all public repositories for the configured GitHub user.
    
    Returns:
        List[Dict]: List of repository data
    """
    repos = []
    page = 1
    rate_limiter = RateLimitHandler()
    
    while True:
        print(f"\nFetching page {page}...")
        url = f"https://api.github.com/users/{GITHUB_USERNAME}/repos?page={page}&per_page=100"
        
        try:
            response = rate_limiter.make_request(url)
            batch = response.json()
            
            if not batch:
                print("No more repositories found")
                break

            print(f"Found {len(batch)} repositories in this batch")
            valid_repos = [
                repo for repo in batch
                if not repo['archived'] and 
                   not repo['private'] and 
                   not repo['fork'] and
                   repo['full_name'] not in EXCLUDE_REPOS
            ]
            print(f"After filtering: {len(valid_repos)} valid repositories")
            repos.extend(valid_repos)
            page += 1
            
        except Exception as e:
            print(f"Error fetching repositories: {str(e)}")
            raise

    repos.sort(key=lambda r: r.get('pushed_at', ''), reverse=True)
    debug_print_repos(repos)
    return repos

def debug_print_repos(repos: List[Dict]) -> None:
    """
    Print repository information for debugging.
    
    Args:
        repos (List[Dict]): List of repository data
    """
    print("\nFetched Repositories:")
    for repo in repos:
        print(f" - {repo['name']} (Fork: {repo['fork']}, Archived: {repo['archived']}, Private: {repo['private']})") 