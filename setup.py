"""
Setup configuration for GitHub Showcase
"""
from setuptools import setup, find_packages

setup(
    name="github-showcase",
    version="2.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "requests>=2.31.0",
        "typing-extensions>=4.5.0",
    ],
    python_requires=">=3.8",
    author="Vijay Kumar Singh",
    author_email="vscit23@gmail.com",
    description="A dynamic GitHub repository showcase generator",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/vsingh55/myGH-showcase",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
) 