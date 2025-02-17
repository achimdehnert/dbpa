"""
Database Personal Assistant (DBPA) - A natural language interface for database management.
"""

from setuptools import setup, find_packages

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith("#")]

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="dbpa",
    version="0.1.0",
    author="Achim Dehnert",
    author_email="achim.dehnert@iil.gmbh",  # Replace with your email
    description="A natural language interface for database management",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/achimdehnert/dbpa",
    project_urls={
        "Bug Tracker": "https://github.com/achimdehnert/dbpa/issues",
        "Documentation": "https://github.com/achimdehnert/dbpa#readme",
        "Source Code": "https://github.com/achimdehnert/dbpa",
    },
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    package_data={
        "dbpa": ["py.typed"],
    },
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
        "Operating System :: OS Independent",
        "Typing :: Typed",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=8.0.0",
            "pytest-cov>=4.1.0",
            "mypy>=1.8.0",
            "black>=24.1.1",
            "isort>=5.13.2",
            "ruff>=0.2.1",
            "pre-commit>=3.6.0",
            "types-all>=1.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "dbpa=dbpa.cli:main",
        ],
    },
    zip_safe=False,  # Required for mypy to find py.typed marker
)
