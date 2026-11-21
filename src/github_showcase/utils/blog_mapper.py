"""
Blog mapping utility for GitHub Showcase
"""
from ..config.settings import BLOG_BASE_URL, BLOG_MAPPING, NO_BLOG_MESSAGE

def get_blog_link(repo_name: str) -> str | None:
    """
    Return the blog URL for a given repository name if mapped, else None.
    """
    slug = BLOG_MAPPING.get(repo_name)
    if slug:
        return f"{BLOG_BASE_URL}/{slug}"
    return None 