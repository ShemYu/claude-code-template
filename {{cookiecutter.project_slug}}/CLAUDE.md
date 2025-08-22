# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Information

- **Project**: {{cookiecutter.project_name}}
- **Package**: {{cookiecutter.package_name}}
- **Version**: {{cookiecutter.version}}
- **Author**: {{cookiecutter.author_name}}

## Development Standards

### Code Style and Formatting
- **Style Guide**: Follow Google style with PEP8 compliance, using modern line length limits (not traditional 79 characters)
- **Documentation**: Use Google-style docstrings for all functions and classes
- **Formatting Tools**: Use `black` for code formatting and `isort` for import sorting (configuration in pyproject.toml)

### Development Environment
- **Dependency Management**: Use `uv` for package management and `uv venv` for virtual environment creation
- **Environment Setup**: 
  - `uv venv` - Create virtual environment
  - `uv add <package>` - Add dependencies
  - `uv sync` - Sync dependencies
- **Code Formatting Commands**:
  - `black .` - Format Python code
  - `isort .` - Sort imports
  - `black . && isort .` - Format code and sort imports together

### Git Workflow
- **Branching Model**: Use Git Flow (master/dev/feat/release/hotfix branches)
- **Branch Naming**: `feat/{feature_name}` for new features
- **Merge Process**: Create merge requests from feat branches to dev branch
- **Code Review**: Require code review for all merge requests
- **Versioning**: Use semantic versioning for releases (v1.0.0)

### Project Organization
- **File Organization**: Structure directories and files consistently
- **Testing**: Establish testing patterns and coverage requirements
- **Security**: Implement authentication patterns and input validation

## General Engineering Principles
- **Clean code focus**: Demonstrate clean coding habits, maintainable code, and design patterns
- **Architectural soundness**: Structure projects for ongoing scalability and reliability
- **Justification requirement**: Every decision must link to tangible constraints, clear benefits, or testable hypotheses
- **Problem-solving demonstration**: Show depth of reasoning over volume of changes
- **Context-aware solutions**: Provide concrete, context-bound reasons rather than generic advice

## Discussion and Design Guidelines

### SOLID Principles Application
- **Single Responsibility Principle (SRP)**: Each class/module should have one reason to change - separate concerns like conversation management from model inference
- **Open/Closed Principle (OCP)**: Design for extension without modification - use interfaces for different model providers or conversation strategies
- **Liskov Substitution Principle (LSP)**: Subtypes must be substitutable for base types - ensure model implementations can be swapped seamlessly
- **Interface Segregation Principle (ISP)**: Clients shouldn't depend on interfaces they don't use - separate large interfaces into focused contracts
- **Dependency Inversion Principle (DIP)**: Depend on abstractions, not concretions - inject dependencies rather than hardcode implementations

### Design Patterns to Consider
- **Strategy Pattern**: For different conversation handling approaches or model selection strategies
- **Factory Pattern**: For creating model instances or conversation managers based on configuration
- **Observer Pattern**: For handling conversation events, logging, or monitoring
- **Adapter Pattern**: For integrating different model APIs or external services
- **Repository Pattern**: For conversation persistence and retrieval abstraction
- **Chain of Responsibility**: For processing conversation middleware (auth, logging, validation)

### Design References and Foundations
- **Domain-Driven Design (DDD)**: Structure around business domains (conversation, user, model) rather than technical layers
- **Hexagonal Architecture**: Keep business logic independent of external concerns (APIs, databases)
- **Clean Architecture**: Separate concerns into layers with clear dependency direction
- **Microservices Patterns**: Consider service boundaries, data consistency, and communication patterns
- **Event-Driven Architecture**: For loosely coupled components and scalable conversation handling