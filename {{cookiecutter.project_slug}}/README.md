# {{cookiecutter.project_name}}

{{cookiecutter.project_description}}

## Development Setup

This project follows the coding standards established in our template.

### Prerequisites

- Python {{cookiecutter.python_version}}+
- uv (for dependency management)

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd {{cookiecutter.project_slug}}
```

2. Create and activate virtual environment:
```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
uv sync
```

### Development Commands

- `uv add <package>` - Add new dependencies
- `black .` - Format code
- `isort .` - Sort imports
- `black . && isort .` - Format and sort imports

## Project Structure

This project follows our established coding standards:
- Google style with PEP8 compliance
- Modern line length limits
- Google-style docstrings
- Git Flow branching model

## Contributing

1. Create a feature branch: `git checkout -b feat/your-feature`
2. Make your changes following our coding standards
3. Format code: `black . && isort .`
4. Create a pull request to the `dev` branch

## Author

{{cookiecutter.author_name}} <{{cookiecutter.author_email}}>