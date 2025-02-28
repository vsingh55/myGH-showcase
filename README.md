# 📚 GitHub RepoHub Showcase

[![GH RepoHub Demo](https://img.shields.io/badge/Demo-Live-green?style=for-the-badge)](https://vsingh55.github.io/myGH-showcase/)
[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)](LICENSE)

## 🌟 Features
- Dynamic GitHub repository showcase
- Automatic content updates via GitHub Actions
- Technology-specific filtering system
- Dark/Light theme toggle
- Automated GitHub Pages deployment

## 🛠️ Technologies Used
| Category        | Technologies                          |
|-----------------|---------------------------------------|
| Core            | Python 3.8+, HTML5, CSS3              |
| APIs            | GitHub REST API                       |
| Deployment      | GitHub Pages, GitHub Actions          |
| Libraries       | Requests, html.escape                 |

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- GitHub account
- GitHub Personal Access Token (public_repo scope)

```bash
# After setting up repo change username and other data in main.py.
website will be live in following  format: 
https://username.github.io/repository_name/

# Maunal setup to generate index.html 
# Clone repository
git clone https://github.com/vsingh55/myGH-showcase.git

# Install dependencies
pip install -r requirements.txt

# Run the generator
python main.py

# Check on local host 
python -m http.server 8000
```

## 🏗️ Project Structure
```
myGH-showcase/
├── main.py                        # Core logic
├── requirements.txt               # Python dependencies
└── .github/
    └──PULL_REQUEST_TEMPLATE.md    # PR Templete
    └── workflows      
        └── deploy.yml             # CI/CD pipelines

```

## 🌈 Current Challenges (Contribution Opportunities)

### 1. Code Structure Improvement
**Goal:** Separate concerns into modular components
```python
# Proposed structure
src/
├── core/                  # Business logic
│   ├── github_api.py
│   └── html_generator.py
├── templates/             # HTML templates
│   └── base.html.j2
├── static/                # CSS/JS assets
│   ├── styles.css
│   └── scripts.js
└── config.py              # Configuration manager
```

### 2. Theme System Enhancement
**Current Issue:** Incomplete dark mode implementation
```css
/* Required Fixes */
[data-theme="dark"] {
    --table-bg: #2d2d2d;
    --text-color: #ffffff;
    --filter-bg: #3a3a3a;
}
```

## 🤝 Contribution Guidelines

### Areas for Contribution
- Frontend component separation
- Theme system improvements
- Performance optimizations
- Additional filtering capabilities
- Enhanced documentation

### How to Contribute
1. Fork the repository
2. Create feature branch: `git checkout -b feat/your-feature`
3. Commit changes: `git commit -m 'Add some feature'`
4. Push to branch: `git push origin feat/your-feature`
5. Open Pull Request


## 📜 License
This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

---

**Maintainer:** [Vijay Kumar Singh](https://github.com/vsingh55)  
**Support:** vscit23@gmail.com


Let's build an amazing repository showcase together! 🚀