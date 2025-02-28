import requests
import os
from html import escape

# Configuration
GITHUB_USERNAME = "vsingh55"
EXCLUDE_REPOS = ["vsingh55/vsingh55"]
OUTPUT_FILE = "index.html"
BLOG_BASE_URL = "https://blogs.vijaysingh.cloud"
TECH_FILTERS = [
    "azure", "aws", "gcp", "docker", "kubernetes", "terraform",
    "ansible", "devsecops", "gitlab", "github-actions", "ci/cd",
    "jenkins", "elk", "prometheus", "grafana", "maven", "trivy",
    "sonarqube", "linux", "git", "slack", "jira", "python",
    "shell-scripting"
]

def format_tech_name(tech):
    replacements = {
        'ci/cd': 'CI/CD',
        'devsecops': 'DevSecOps',
        'github-actions': 'GitHub Actions',
        'shell-scripting': 'Shell Scripting'
    }
    return replacements.get(tech, tech.replace('-', ' ').title())

def get_blog_link(repo_name):
    slug = repo_name.lower().replace('_', '')  
    return f"{BLOG_BASE_URL}/{slug}" if slug else f"{BLOG_BASE_URL}/series/projects"

def debug_print_repos(repos):
    print("\nFetched Repositories:")
    for repo in repos:
        print(f" - {repo['name']} (Fork: {repo['fork']}, Archived: {repo['archived']}, Private: {repo['private']})")

def get_all_repositories():
    repos = []
    page = 1
    while True:
        print(f"\nFetching page {page}...")
        url = f"https://api.github.com/users/{GITHUB_USERNAME}/repos?page={page}&per_page=100"
        response = requests.get(url)

        if response.status_code != 200:
            print(f"API Error! Status Code: {response.status_code}")
            print(f"Response: {response.text}")
            raise Exception("Failed to fetch repositories")

        batch = response.json()
        if not batch:
            print("No more repositories found")
            break

        print(f"Found {len(batch)} repositories in this batch")
        valid_repos = [
            repo for repo in batch
            if not repo['fork'] and
               repo['full_name'] not in EXCLUDE_REPOS and
               not repo['archived'] and
               not repo['private']
        ]
        print(f"After filtering: {len(valid_repos)} valid repositories")
        repos.extend(valid_repos)
        page += 1

    debug_print_repos(repos)
    return repos

def generate_html_table(repos):
    html = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>GH RepoHub</title>
    <style>
        /* ======== THEME VARIABLES ======== */
        :root {
            --bg-color: #ffffff;
            --text-color: #333333;
            --header-bg: linear-gradient(270deg, #0366d6, #28a745, #6f42c1);
            --card-bg: #f8f9fa;
            --border-color: #ddd;
            --tag-bg: #f1f8ff;
        }

        [data-theme="dark"] {
            --bg-color: #1a1a1a;
            --text-color: #e0e0e0;
            --header-bg: linear-gradient(270deg, #004792, #1e7d34, #4b2d7f);
            --card-bg: #2d2d2d;
            --border-color: #404040;
            --tag-bg: #2a4365;
        }

        /* ======== BASE STYLES ======== */
        body {
            margin: 0;
            padding: 20px;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
            background-color: var(--bg-color);
            color: var(--text-color);
            transition: background-color 0.3s, color 0.3s;
        }

         /* ======== HEADER & BADGES ======== */
        .page-title {
            background: var(--header-bg);
            background-size: 600% 600%;
            animation: title-gradient 8s ease infinite;
            color: white;
            padding: 20px;
            text-align: center;
            border-radius: 8px;
            margin-bottom: 20px;
            width: 100%;
        }

        .badge-container {
            width: 70%;
            margin-left: auto;
            margin-bottom: 30px;
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
            justify-content: flex-end;
        }

        .badge-container img {
            height: 24px;
            transition: transform 0.2s ease;
        }

        .badge-container img:hover {
            transform: translateY(-2px);
        }

        /* ======== THEME TOGGLE ======== */
        .theme-toggle {
            position: fixed;
            bottom: 20px;
            right: 20px;
            padding: 10px 15px;
            border-radius: 20px;
            border: none;
            background: var(--card-bg);
            color: var(--text-color);
            cursor: pointer;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }

        /* ======== TITLE STYLES ======== */
        .page-title {
            background: var(--header-bg);
            background-size: 600% 600%;
            animation: title-gradient 8s ease infinite;
            color: white;
            padding: 20px;
            text-align: center;
            border-radius: 8px;
            margin: 0;
            flex-grow: 1;
            max-width: 70%;
        }

        # body {
        #     margin: 0;
        #     padding: 20px;
        #     font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
        # }
        # .connect-me {
        #     margin-top: 20px;
        # }
        # .connect-me a {
        #     margin-right: 10px;
        # }
        
        # @keyframes title-gradient {
        #     0% { background-position: 0% 50%; }
        #     50% { background-position: 100% 50%; }
        #     100% { background-position: 0% 50%; }
        # }


        /* ======== EXISTING COMPONENTS ======== */
        .main-container {
            display: flex;
            gap: 20px;
            max-width: 100%;
        }

        .filter-section {
            flex: 0 0 150px;
            background: #f8f9fa;
            padding: 15px;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            height: fit-content;
            position: sticky;
            top: 20px;
        }

        .content-section {
            flex: 1;
        }

        .info-banner {
            background-color: #f1f8ff;
            border: 1px solid #c8e1ff;
            border-radius: 6px;
            padding: 12px;
            margin-bottom: 20px;
        }

        .filter-group {
            margin: 10px 0;
        }

        .filter-group label {
            display: flex;
            align-items: center;
            gap: 8px;
            cursor: pointer;
        }

        .filter-group input[type="checkbox"] {
            cursor: pointer;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
            background: white;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }

        th, td {
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }

        th {
            background-color: #f2f2f2;
            position: sticky;
            top: 0;
            z-index: 1;
        }

        input[type="text"] {
            padding: 8px;
            width: 100%;
            margin-bottom: 20px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }

        a {
            color: #0366d6;
            text-decoration: none;
        }

        a:hover {
            text-decoration: underline;
        }

        .tag {
            display: inline-block;
            background-color: #f1f8ff;
            padding: 5px 10px;
            margin: 2px;
            border-radius: 3px;
            font-size: 12px;
        }

        @media (max-width: 768px) {
            .badge-container {
                width: 100%;
                justify-content: center;
            }
        }

        #     .filter-section {
        #         position: static;
        #         width: auto;
        #     }
        # }
        
        # .filter-section {
        #     background: var(--card-bg);
        #     box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        # }

        # th {
        #     background-color: var(--card-bg);
        # }

        # .tag {
        #     background-color: var(--tag-bg);
        # }

        # input[type="text"] {
        #     border: 1px solid var(--border-color);
        # }
        
    </style>
</head>
<body>
    <!-- Title Section -->
    <h1 class="page-title">Cloud & DevOps Projects RepoHub</h1>

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

    <!-- Theme Toggle -->
    <button class="theme-toggle" onclick="toggleTheme()">🌓 Toggle Theme</button>
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
        blog_url = get_blog_link(repo['name'])

        html += f"""                    <tr data-tags="{','.join(tags).lower()}">
                        <td><a href="{repo['html_url']}" target="_blank" title="View GitHub Repository">{name}</a></td>
                        <td>{description}</td>
                        <td>{f'<a href="{homepage}" target="_blank">Website</a>' if homepage else ''}</td>
                        <td>{"".join([f'<span class="tag">{escape(tag)}</span>' for tag in tags])}</td>
                        <td>{f'<a href="{blog_url}" target="_blank">Read Blog</a>' if blog_url else 'Coming Soon'}</td>
                    </tr>
"""

    html += """                </tbody>
            </table>
        </div>
    </div>

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

        // Existing search/filter functions 
        function searchTable() {
            const searchTerm = document.getElementById('searchInput').value.toLowerCase();
            const rows = document.querySelectorAll('tbody tr');

            rows.forEach(row => {
                const rowText = row.textContent.toLowerCase();
                row.style.display = rowText.includes(searchTerm) ? '' : 'none';
            });
        }

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

def main():
    repos = get_all_repositories()
    html = generate_html_table(repos)

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"HTML table generated successfully at {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
