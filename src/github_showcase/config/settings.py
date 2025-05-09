"""
Configuration settings for GitHub Showcase
"""

# GitHub Configuration
GITHUB_USERNAME = "vsingh55"
EXCLUDE_REPOS = ["vsingh55/vsingh55"]
OUTPUT_FILE = "index.html"
BLOG_BASE_URL = "https://blogs.vijaysingh.cloud"

# Technology Filters
TECH_FILTERS = [
    "azure", "aws", "gcp", "docker", "kubernetes", "terraform",
    "ansible", "devsecops", "gitlab", "github-actions", "ci/cd",
    "jenkins", "elk", "prometheus", "grafana", "maven", "trivy",
    "sonarqube", "linux", "git", "slack", "jira", "python",
    "shell-scripting"
]

# Blog Mapping Configuration
BLOG_MAPPING = {
    # Add your blog mappings here
    # Format: "repository-name": "blog-slug"
    "NBA-Analytics-Data-Lake": "data-lake",
    # Add more mappings as needed
}

# UI Configuration
THEME_CONFIG = {
    "light": {
        "bg_color": "#ffffff",
        "text_color": "#333333",
        "header_bg": "linear-gradient(270deg, #0366d6, #28a745, #6f42c1)",
        "card_bg": "#f8f9fa",
        "border_color": "#ddd",
        "tag_bg": "#f1f8ff",
        "table_bg": "#ffffff",
        "filter_bg": "#f8f9fa"
    },
    "dark": {
        "bg_color": "#1a1a1a",
        "text_color": "#ffffff",
        "header_bg": "linear-gradient(270deg, #004792, #1e7d34, #4b2d7f)",
        "card_bg": "#2d2d2d",
        "border_color": "#404040",
        "tag_bg": "#2a4365",
        "table_bg": "#2d2d2d",
        "filter_bg": "#3a3a3a"
    }
}

# Messages
NO_BLOG_MESSAGE = "Coming Soon" 