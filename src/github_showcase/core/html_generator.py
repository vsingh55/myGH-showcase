"""
HTML generator for GitHub Showcase
"""
from html import escape
from typing import List, Dict
from ..config.settings import TECH_FILTERS, THEME_CONFIG
from ..utils.blog_mapper import get_blog_link, BLOG_MAPPING

def format_tech_name(tech: str) -> str:
    """
    Format technology name for display.
    
    Args:
        tech (str): Technology name
        
    Returns:
        str: Formatted technology name
    """
    replacements = {
        'ci/cd': 'CI/CD',
        'devsecops': 'DevSecOps',
        'github-actions': 'GitHub Actions',
        'shell-scripting': 'Shell Scripting'
    }
    return replacements.get(tech, tech.replace('-', ' ').title())

def generate_html_table(repos: List[Dict]) -> str:
    """
    Generate HTML table from repository data.
    
    Args:
        repos (List[Dict]): List of repository data
        
    Returns:
        str: Generated HTML
    """
    html = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>GH RepoHub</title>
    <style>
        :root {
            --bg-color: #f5f6fa;
            --text-color: #23272f;
            --header-bg: linear-gradient(270deg, #4e54c8, #8f94fb);
            --card-bg: #fff;
            --border-color: #e0e0e0;
            --tag-bg: #e3eafc;
            --table-bg: #fff;
            --filter-bg: #f0f2f7;
            --search-border: #4e54c8;
            --table-header-bg: #f0f2f7;
            --table-row-hover: #f5f5f5;
            --accent: #4e54c8;
        }
        [data-theme="dark"] {
            --bg-color: #181A20;
            --text-color: #F1F1F1;
            --header-bg: linear-gradient(270deg, #23286b, #1e7d34, #4b2d7f);
            --card-bg: #23242b;
            --border-color: #23242b;
            --tag-bg: #232d3b;
            --table-bg: #23242b;
            --filter-bg: #23242b;
            --search-border: #8f94fb;
            --table-header-bg: #232d3b;
            --table-row-hover: #232d3b;
            --accent: #8f94fb;
        }
        html {
            font-size: 18px;
        }
        body {
            max-width: 100vw;
            overflow-x: hidden;
            font-size: 1rem;
            margin: 0;
            padding: 0.3rem;
            background-color: var(--bg-color);
            color: var(--text-color);
            font-family: 'Inter', 'Segoe UI', 'Roboto', 'Helvetica Neue', Arial, sans-serif;
            transition: background-color 0.3s, color 0.3s;
        }
        .page-title {
            background: linear-gradient(90deg, #ff9966, #ff5e62, #36d1c4, #5b86e5, #36d1c4, #ff9966);
            background-size: 200% 200%;
            animation: gradient-move 8s ease-in-out infinite;
            color: white;
            padding: 0.6rem 1rem 0.6rem 1rem;
            text-align: center;
            border-radius: 12px;
            margin-bottom: 0.5rem;
            width: 100%;
            font-size: 2.8rem;
            font-weight: 900;
            letter-spacing: 1px;
            box-shadow: 0 4px 24px 0 rgba(0,0,0,0.10);
            position: relative;
        }
        @keyframes gradient-move {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        .page-title .animated-text {
            display: inline-block;
            background: linear-gradient(90deg, #ff9966, #36d1c4, #5b86e5, #ff5e62);
            background-size: 400% 400%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: text-gradient-move 6s ease-in-out infinite;
        }
        @keyframes text-gradient-move {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        .badge-container {
            width: 100%;
            margin-left: auto;
            margin-top: 1rem;
            margin-bottom: 1rem;
            display: flex;
            gap: 0.75rem;
            flex-wrap: wrap;
            justify-content: flex-end;
        }
        .badge-container img {
            height: 1.6rem;
            transition: transform 0.2s ease;
        }
        .badge-container img:hover {
            transform: translateY(-2px) scale(1.08);
        }
        .theme-toggle {
            position: fixed;
            bottom: 1.5rem;
            right: 1.5rem;
            padding: 0.75rem 1.2rem;
            border-radius: 24px;
            border: none;
            background: var(--card-bg);
            color: var(--text-color);
            cursor: pointer;
            box-shadow: 0 2px 8px rgba(0,0,0,0.12);
            z-index: 1000;
            font-weight: 600;
        }
        .main-container {
            display: flex;
            flex-direction: row;
            gap: 2rem;
            width: 100vw;
            max-width: none;
            margin: 0;
            padding: 0 0.5rem 2rem 0.5rem;
            align-items: flex-start;
        }
        .filter-section {
            min-width: 220px;
            background: var(--filter-bg);
            padding: 1.5rem 1rem 1rem 1rem;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.10);
            height: fit-content;
            color: var(--text-color);
            font-size: 1.05rem;
            font-weight: 500;
            border-right: 1px solid var(--border-color);
            flex-shrink: 0;
            position: sticky;
            top: 1.5rem;
            z-index: 10;
            max-height: 90vh;
            overflow-y: auto;
        }
        .content-section {
            flex: 1 1 0%;
            background: var(--card-bg);
            border-radius: 12px;
            box-shadow: 0 2px 12px rgba(0,0,0,0.10);
            padding: 2rem 2rem 2rem 2rem;
            min-width: 0;
        }
        .info-banner, #searchInput {
            max-width: 900px;
            margin: 0 auto 1.2rem auto;
            display: block;
        }
        table {
            table-layout: auto;
            width: 100%;
            overflow-x: auto;
            font-size: 1rem;
            border-collapse: collapse;
            margin-top: 1.2rem;
            background: var(--table-bg);
            box-shadow: 0 1px 6px rgba(0,0,0,0.08);
            border-radius: 8px;
        }
        th, td {
            font-size: 1rem;
            padding: 0.8rem 0.6rem;
            text-align: left;
            border-bottom: 1px solid var(--border-color);
            color: var(--text-color);
        }
        th {
            background-color: var(--table-header-bg);
            position: sticky;
            top: 0;
            z-index: 1;
            font-weight: 700;
            letter-spacing: 0.5px;
        }
        tr:hover {
            background-color: var(--table-row-hover);
        }
        .info-banner {
            background-color: var(--accent);
            border: 1px solid var(--accent);
            border-radius: 8px;
            padding: 1rem 1.2rem;
            margin-bottom: 1.2rem;
            color: #fff;
            font-size: 1.08rem;
            font-weight: 500;
            box-shadow: 0 1px 6px rgba(0,0,0,0.08);
        }
        [data-theme="dark"] .info-banner {
            background-color: var(--accent);
            border: 1px solid var(--accent);
            color: #181A20;
        }
        .filter-group {
            margin: 0.7rem 0;
        }
        .filter-group label {
            display: flex;
            align-items: center;
            gap: 0.6rem;
            cursor: pointer;
            color: var(--text-color);
            font-size: 1rem;
        }
        input[type="text"] {
            padding: 0.7rem;
            width: 100%;
            margin-bottom: 1.2rem;
            border: 2px solid var(--search-border);
            border-radius: 6px;
            background: var(--card-bg);
            color: var(--text-color);
            font-size: 1rem;
        }
        input[type="text"]:focus {
            outline: none;
            border-color: var(--accent);
        }
        a {
            color: var(--accent);
            text-decoration: none;
            font-weight: 500;
        }
        a:hover {
            text-decoration: underline;
        }
        .tag {
            display: inline-block;
            background-color: var(--tag-bg);
            padding: 0.4rem 0.8rem;
            margin: 2px;
            border-radius: 4px;
            font-size: 0.95rem;
            color: var(--text-color);
            font-weight: 500;
            box-shadow: 0 1px 3px rgba(0,0,0,0.04);
        }
        th:nth-child(1), td:nth-child(1) {
            min-width: 120px;
            width: 13%;
        }
        th:nth-child(4), td:nth-child(4) {
            min-width: 260px;
            width: 28%;
        }
        th:nth-child(2), td:nth-child(2) {
            min-width: 300px;
            width: 35%;
        }
        @media (max-width: 900px) {
            html {
                font-size: 14px;
            }
            .main-container {
                flex-direction: column;
                gap: 0;
                padding: 0 0.5rem;
                align-items: stretch;
            }
            .content-section, .filter-section {
                padding: 0.8rem 0.2rem;
            }
            .filter-section {
                min-width: 0;
                border-right: none;
                border-bottom: 1px solid var(--border-color);
            }
            th:nth-child(1), td:nth-child(1) {
                min-width: 100px;
                width: 18%;
            }
            th:nth-child(4), td:nth-child(4) {
                min-width: 120px;
                width: 25%;
            }
        }
        @media (max-width: 600px) {
            html {
                font-size: 15px;
            }
            .page-title {
                font-size: 1.2rem;
                padding: 1rem 0.2rem;
            }
            th, td {
                font-size: 0.95rem;
                padding: 0.5rem 0.2rem;
            }
        }
        @media (min-width: 1800px) {
            .main-container {
                max-width: 1700px;
                margin: 0 auto;
            }
        }
    </style>
</head>
<body>
    <!-- Title Section -->
    <h1 class="page-title"><span class="animated-text">My GitHub Portfolio</span></h1>

    <!-- Badges Container -->
    <div class="badge-container">
        <a href="https://vijaysingh.cloud" target="_blank">
            <img src="https://img.shields.io/badge/visit_my_Portfolio-%23000000.svg?style=for-the-badge&logo=firefox&logoColor=#FF7139" alt="Portfolio">
        </a>
        <a href="https://www.linkedin.com/in/vsingh55/" target="_blank">
            <img src="https://img.shields.io/badge/Let's_connect_🤝-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
        </a>
        <a href="https://blogs.vijaysingh.cloud/" target="_blank">
            <img src="https://img.shields.io/badge/-Visit_my_Blogs-034efc?style=for-the-badge&logo=hashnode&logoColor=white" alt="Blog">
        </a>
        <a href="https://x.com/vsingh_55" target="_blank">
            <img src="https://img.shields.io/badge/-@Follow_me-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white" alt="Twitter">
        </a>
        <a href="mailto:vscit23@gmail.com">
            <img src="https://img.shields.io/badge/-mail_me_-a284e8?style=for-the-badge&logo=gmail&logoColor=white" alt="Email">
        </a>
    </div>

    <!-- Main Content -->
    <div class="main-container">
        <div class="filter-section">
            <h3>Filter by Technology:</h3>
"""

    # Add filter checkboxes
    for tech in TECH_FILTERS:
        html += f'            <div class="filter-group"><label><input type="checkbox" value="{tech}"> {format_tech_name(tech)}</label></div>\n'

    html += """
        </div>

        <div class="content-section">
            <div class="info-banner">
                💡 Click on project names to view their respective GH repositories. Each project includes detailed documentation, code, setup guide & visit Blog page to detailed implementation steps.
            </div>

            <input type="text" id="searchInput" placeholder="Search across all content..." onkeyup="searchTable()">

            <table>
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Description</th>
                        <th>Website</th>
                        <th>Tags</th>
                        <th>Blog</th>
                    </tr>
                </thead>
                <tbody>
"""

    for repo in repos:
        name = escape(repo['name'])
        description = escape(repo['description'] or '')
        homepage = escape(repo['homepage'] or '')
        tags = repo['topics'] if 'topics' in repo else []
        # Only show 'Read Blog' if the repo is explicitly mapped in BLOG_MAPPING
        blog_mapped = repo['name'] in BLOG_MAPPING
        blog_url = get_blog_link(repo['name']) if blog_mapped else ''
        html += f"""                    <tr data-tags="{','.join(tags).lower()}">
                        <td><a href="{repo['html_url']}" target="_blank" title="View GitHub Repository">{name}</a></td>
                        <td>{description}</td>
                        <td>{f'<a href="{homepage}" target="_blank">Website</a>' if homepage else ''}</td>
                        <td>{"".join([f'<span class="tag">{escape(tag)}</span>' for tag in tags])}</td>
                        <td>{f'<a href="{blog_url}" target="_blank">Read Blog</a>' if blog_mapped else 'Coming Soon'}</td>
                    </tr>
"""

    html += """                </tbody>
            </table>
        </div>
    </div>

    <!-- Theme Toggle -->
    <button class="theme-toggle" onclick="toggleTheme()">🌓 Toggle Theme</button>

    <script>
        // Theme Management
        function toggleTheme() {
            const body = document.body;
            const currentTheme = body.getAttribute('data-theme');
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            body.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
        }

        // Initialize theme
        const savedTheme = localStorage.getItem('theme') || 'light';
        document.body.setAttribute('data-theme', savedTheme);

        // Search functionality
        function searchTable() {
            const searchTerm = document.getElementById('searchInput').value.toLowerCase();
            const rows = document.querySelectorAll('tbody tr');

            rows.forEach(row => {
                const rowText = row.textContent.toLowerCase();
                row.style.display = rowText.includes(searchTerm) ? '' : 'none';
            });
        }

        // Filter functionality
        document.querySelectorAll('.filter-section input').forEach(checkbox => {
            checkbox.addEventListener('change', () => {
                const selectedTech = Array.from(document.querySelectorAll('.filter-section input:checked'))
                    .map(cb => cb.value.toLowerCase());

                const rows = document.querySelectorAll('tbody tr');
                rows.forEach(row => {
                    const tags = row.getAttribute('data-tags').split(',');
                    const hasTech = selectedTech.length === 0 ||
                                  selectedTech.some(tech => tags.includes(tech));
                    row.style.display = hasTech ? '' : 'none';
                });
            });
        });
    </script>
</body>
</html>"""
    return html 