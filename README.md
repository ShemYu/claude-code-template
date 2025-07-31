# claude-code-template

A cookiecutter template for Python projects with my personal coding standards.

## Features

- Google style with PEP8 compliance
- Modern line length limits (100 characters)
- Google-style docstrings
- uv for dependency management
- black and isort for code formatting
- Git Flow branching model
- Comprehensive CLAUDE.md for AI assistance

## Usage

### Prerequisites

Install cookiecutter:
```bash
pip install cookiecutter
# or
uv tool install cookiecutter
```

### Create a new project

```bash
cookiecutter https://github.com/ShemYu/claude-code-template.git
```

Or from local directory:
```bash
cookiecutter /path/to/claude-code-template
```

### Template Variables

- `project_name`: Human-readable project name
- `project_slug`: URL/directory-safe project name
- `package_name`: Python package name
- `project_description`: Brief project description
- `author_name`: Your name
- `author_email`: Your email address
- `version`: Initial version (default: 0.1.0)
- `python_version`: Python version requirement (default: 3.11)
- `use_git`: Initialize git repository (default: y)
- `create_dev_branch`: Create development branch (default: y)

## Generated Project Structure

```
your-project/
├── README.md
├── pyproject.toml
├── CLAUDE.md
├── .gitignore
└── your_package/
    ├── __init__.py
    └── main.py
```

## Post-Generation Setup

1. Navigate to your new project:
   ```bash
   cd your-project
   ```

2. Create virtual environment:
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install development dependencies:
   ```bash
   uv add --dev black isort
   ```

4. If git initialization was enabled, set up your repository:
   ```bash
   git remote add origin <your-repo-url>
   git push -u origin main
   ```

## Template Development

This is a personal coding template that establishes standards for future projects.
