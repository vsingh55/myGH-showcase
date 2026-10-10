"""
Main entry point for GitHub Showcase
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(override=True)  # override=True ensures .env values take precedence

from .utils.github_api import get_all_repositories
from .core.html_generator import generate_html_table
from .config.settings import OUTPUT_FILE

def main():
    """
    Main function to generate the GitHub Showcase
    """
    # Fetch repositories
    repos = get_all_repositories()
    
    # Generate HTML
    html = generate_html_table(repos)
    
    # Write to file
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"HTML table generated successfully at {OUTPUT_FILE}")

if __name__ == "__main__":
    main() 