# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Core Concepts

**Code Style Standards:**
- Follow Google style with PEP8 compliance
- Use modern line length limits (not traditional 79 characters)
- Apply Google-style docstrings for all functions and classes

**Development Environment:**
- Use `uv` for dependency management
- Use `uv venv` for virtual environment creation and management
- Use `black` for code formatting and `isort` for import sorting

**Git Workflow:**
- Follow Git Flow branching model with `master`, `dev`, `feat`, `release`, `hotfix` branches
- Branch naming: `feat/{feature_name}` for features
- All merge requests require code review
- Use semantic versioning for tags (v1.0.0)

## Project Information

- **Project**: {{cookiecutter.project_name}}
- **Package**: {{cookiecutter.package_name}}
- **Version**: {{cookiecutter.version}}
- **Author**: {{cookiecutter.author_name}}

## Development Setup

### Environment Setup
- `uv venv` - Create virtual environment
- `uv add <package>` - Add dependencies
- `uv sync` - Sync dependencies

### Code Formatting and Linting
- `black .` - Format Python code
- `isort .` - Sort imports
- `black . && isort .` - Format code and sort imports together

## Coding Standards

- **Code Style**: Follow Google style with PEP8 compliance, but use modern line length limits (not the traditional 79 characters)
- **Code Formatting**: Use `black` for automatic code formatting and `isort` for import sorting (configuration in pyproject.toml)
- **Documentation**: Use Google-style docstrings for all functions and classes
- **Dependencies**: Use uv for dependency management and uv venv for virtual environment creation and management
- **File Organization**: Structure directories and files consistently
- **Testing**: Establish testing patterns and coverage requirements
- **Git Workflow**: 
  - Use Git Flow branching model (master/dev/feat/release/hotfix)
  - Branch naming: `feat/{feature_name}` for new features
  - Create merge requests from feat branches to dev branch
  - Require code review for all merge requests
  - Use semantic versioning for releases (v1.0.0)
- **Security**: Implement authentication patterns and input validation