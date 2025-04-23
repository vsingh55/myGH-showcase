#  GitHub RepoHub Showcase

[![GH RepoHub Demo](https://img.shields.io/badge/Demo-Live-green?style=for-the-badge)](https://vsingh55.github.io/myGH-showcase/)

<details>
<summary>Quick Navigation</summary>

- [GitHub RepoHub Showcase](#github-repohub-showcase)
  - [Project Overview](#project-overview)
    - [Objective](#objective)
    - [Executive Summary](#executive-summary)
  - [Architecture](#architecture)
    - [Component Breakdown](#component-breakdown)
  - [Technologies Used](#technologies-used)
  - [Project Structure](#project-structure)
    - [Folder Purpose Explanation](#folder-purpose-explanation)
  - [Prerequisites](#prerequisites)
    - [System Requirements](#system-requirements)
    - [Credentials Needed](#credentials-needed)
  - [Installation](#installation)
    - [Quick Start](#quick-start)
  - [Configuration](#configuration)
  - [Deployment](#deployment)
  - [Screenshots](#screenshots)
  - [Live Project](#live-project)
    - [Access Information](#access-information)
  - [Performance Metrics](#performance-metrics)
    - [Key Performance Indicators](#key-performance-indicators)
  - [Security Considerations](#security-considerations)
  - [Troubleshooting](#troubleshooting)
    - [Common Issues and Solutions](#common-issues-and-solutions)
  - [Contributing](#contributing)
    - [Contribution Process](#contribution-process)
  - [License](#license)

</details>

## Project Overview

### Objective

- Create an automated system for showcasing GitHub repositories in an organized and filterable interface
- Solve the challenge of portfolio presentation for developers who maintain multiple projects
- Implement continuous deployment to eliminate manual updates when new repositories are created

### Executive Summary
GitHub RepoHub Showcase is a dynamic web application that automatically generates an elegant portfolio of GitHub repositories. It leverages the GitHub API to fetch repository data, transforms it into a responsive HTML interface, and deploys it to GitHub Pages through automated CI/CD workflows. The system features technology-based filtering, theme customization, and blog integration, making it an ideal solution for developers, teams, and organizations wanting to showcase their projects effectively.

## Architecture
The application follows a serverless architecture with GitHub Pages hosting the static frontend. The backend processing occurs during the CI/CD pipeline execution, where Python scripts fetch repository data and generate the HTML content.
![alt text](/Images/architechture.png)
### Component Breakdown
- **Data Retrieval**: Python script connects to GitHub API to fetch repository information
- **HTML Generation**: Repository data is processed and converted into an interactive HTML page
- **CI/CD Pipeline**: GitHub Actions workflow automates the build and deployment process
- **Static Hosting**: GitHub Pages serves the generated content with no additional infrastructure required
- **Client-Side Processing**: JavaScript handles filtering, searching, and theme switching on the user's browser

## Technologies Used
| Category        | Technologies                          |
|-----------------|---------------------------------------|
| Backend         | Python 3.8+                           |
| Frontend        | HTML5, CSS3, JavaScript               |
| APIs            | GitHub REST API                       |
| CI/CD           | GitHub Actions                        |
| Deployment      | GitHub Pages                          |
| Libraries       | Requests, html.escape                 |

## Project Structure
```
myGH-showcase/
├── main.py                        # Core logic for fetching repos and generating HTML
├── requirements.txt               # Python dependencies (requests)
├── index.html                     # Generated output (not in repository)
└── .github/
    ├── PULL_REQUEST_TEMPLATE.md   # Template for contributions
    └── workflows/
        └── deploy.yml             # GitHub Actions workflow for deployment
```

### Folder Purpose Explanation
- `main.py`: Contains the core application logic for API interaction and HTML generation
- `requirements.txt`: Lists Python dependencies required for the application
- `.github/workflows/`: Contains CI/CD pipeline configurations for automated deployment
- `.github/PULL_REQUEST_TEMPLATE.md`: Standardizes contribution format for project maintainability

##  Prerequisites

### System Requirements
- Python 3.8+ for local development
- Git for version control
- GitHub account for repository access and GitHub Pages hosting

### Credentials Needed

- Repository owner permissions for enabling GitHub Pages
- Write permissions to the repository for CI/CD workflow execution

## Installation

### Quick Start
```bash
# Clone the repository
git clone https://github.com/vsingh55/myGH-showcase.git
cd myGH-showcase

# Install dependencies
pip install -r requirements.txt

# Run the generator locally
python main.py

# Preview the generated site
python -m http.server 8000  # Access at http://localhost:8000
```

## Configuration
The application can be configured by modifying the variables in `main.py`:

```python
# Configuration
GITHUB_USERNAME = "your-username"  # Set to your GitHub username
EXCLUDE_REPOS = ["repos-to-exclude"]  # Repositories to exclude from display
BLOG_BASE_URL = "https://yourblog.com"  # Base URL for blog integration
TECH_FILTERS = [  # Technologies for filtering system
    "azure", "aws", "python", "kubernetes", 
    # Add or remove technologies as needed
]
```

Theme customization can be achieved by modifying the CSS variables in the HTML template section of `main.py`:

```css
:root {
    --bg-color: #ffffff;
    --text-color: #333333;
    /* Customize additional variables */
}
```

## Deployment
Deployment is fully automated through GitHub Actions. The workflow is configured in `.github/workflows/deploy.yml`.

1. **Initial Setup**:
   - Fork or clone the repository
   - Update configuration variables in `main.py`
   - Push changes to the main branch

2. **Automated Process**:
   - GitHub Actions workflow is triggered on push to main branch
   - Python environment is set up with required dependencies
   - `main.py` is executed to generate `index.html`
   - Generated content is published to GitHub Pages branch

3. **Verification**:
   - After successful deployment, the site is available at `https://username.github.io/repository-name/`
   - Check GitHub Actions logs for any deployment issues

## Screenshots
![alt text](/Images/image.png)

##  Live Project

[![GH RepoHub Demo](https://img.shields.io/badge/Demo-Live-green?style=for-the-badge)](https://vsingh55.github.io/myGH-showcase/)

### Access Information

- The showcase is publicly accessible with no authentication required
- Repository links direct to the corresponding GitHub repositories
- Blog links connect to associated technical articles (if configured)
- Website links connect to associated pages (if configured). I have configured website link with the links of my project listed on my portfolio.

## Performance Metrics

### Key Performance Indicators

- **Automation Efficiency**: Eliminates manual portfolio updates
- **Search Optimization**: Provides instant filtering across all repositories
- **Deployment Speed**: GitHub Actions pipeline completes in less than 30 seconds.
- **Page Load Performance**: Static hosting ensures fast load times (<1s on broadband)
- **Content Freshness**: Automatically incorporates newly created repositories

## Security Considerations

- GitHub API token should be stored as a repository secret, not hardcoded if needed
- The application only accesses public repository data
- No user data is collected or stored during browsing
- Content Security Policy considerations for GitHub Pages hosting
- Regular dependency updates to address potential vulnerabilities

## Troubleshooting

### Common Issues and Solutions

- **API Rate Limiting**: If encountering GitHub API rate limits, configure with a personal access token
- **Missing Repositories**: Verify repository visibility settings and check exclusion list
- **Deployment Failures**: Check GitHub Actions logs for specific error messages
- **Local Testing Issues**: Ensure Python version compatibility and proper dependency installation
- **Contact Support**: For additional assistance, contact vscit23@gmail.com

## Contributing
The project welcomes contributions in several key areas:

1. **Code Structure Improvement**
   - Separate concerns into modular components
   - Implement template system instead of string concatenation
   - Create a configuration manager for easier customization

2. **Theme System Enhancement**
   - Complete dark mode implementation
   - Add more theme options
   - Improve accessibility features

3. **Feature Additions**
   - Repository statistics visualization
   - Contribution graph integration
   - Custom sorting options for repositories

### Contribution Process
1. Fork the repository
2. Create a feature branch: `git checkout -b feat/your-feature`
3. Commit changes: `git commit -m 'Add some feature'`
4. Push to branch: `git push origin feat/your-feature`
5. Open a Pull Request following the template

## License
This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

---

**Maintainer:** [Vijay Kumar Singh](https://github.com/vsingh55)  
**Contact:** vscit23@gmail.com

Let's build an amazing repository showcase together! 🚀
