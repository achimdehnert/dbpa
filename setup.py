"""
Database Personal Assistant (DBPA) - A natural language interface for database management.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="dbpa",
    version="0.1.0",
    author="Achim Dehnert",
    author_email="your.email@example.com",  # Replace with your email
    description="A natural language interface for database management",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/achimdehnert/dbpa",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Database :: Database Engines/Servers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "streamlit>=1.24.0",
        "pandas>=1.5.0",
        "psycopg2-binary>=2.9.0",
        "python-dotenv>=1.0.0",
        "openai>=1.0.0",
        "langchain>=0.1.0",
        "langchain-community>=0.0.10",
        "langchain-openai>=0.0.3",
        "langchain-groq>=0.0.1",
        "faiss-cpu>=1.7.0",
    ],
    entry_points={
        "console_scripts": [
            "dbpa=dbpa.cli:main",
        ],
    },
)
