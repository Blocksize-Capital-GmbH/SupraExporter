# Contributing to Supra Blockchain Metrics Exporter

Thank you for your interest in contributing to the Supra Blockchain Metrics Exporter! This document provides guidelines and information for contributors.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Contributing Process](#contributing-process)
- [Code Standards](#code-standards)
- [Testing](#testing)
- [Documentation](#documentation)
- [Submitting Changes](#submitting-changes)

## Code of Conduct

By participating in this project, you agree to abide by our Code of Conduct:

- Be respectful and inclusive
- Focus on constructive feedback
- Accept responsibility for mistakes
- Help create a welcoming environment for all contributors

## Getting Started

### Types of Contributions

We welcome the following types of contributions:

- **Bug Reports**: Help us identify and fix issues
- **Feature Requests**: Suggest new functionality or improvements
- **Code Contributions**: Submit bug fixes, new features, or optimizations
- **Documentation**: Improve or expand project documentation
- **Testing**: Add test cases or improve test coverage

### Before You Start

1. Check existing [issues](https://github.com/blocksize-capital-gmbh/supra-blockchain-metrics-exporter/issues) to avoid duplicates
2. For major changes, open an issue first to discuss the approach
3. Make sure you understand the project's architecture and goals

## Development Setup

### Prerequisites

- Python 3.10 or higher
- [Poetry](https://python-poetry.org/docs/#installation) for dependency management
- [Git](https://git-scm.com/) for version control
- [Docker](https://www.docker.com/) (optional, for testing containerization)

### Environment Setup

1. **Fork and clone the repository**:

    ```bash
    git clone https://github.com/YOUR_USERNAME/supra-blockchain-metrics-exporter.git
    cd supra-blockchain-metrics-exporter
    ```

2. **Install dependencies**:

    ```bash
    poetry install
    ```

3. **Set up pre-commit hooks**:

    ```bash
    poetry run pre-commit install
    ```

4. **Create a test environment**:

    ```bash
    cp .env.example .env
    # Edit .env with test configuration
    ```

5. **Verify setup**:
    ```bash
    poetry run pytest
    ```

## Contributing Process

### 1. Create an Issue

For bugs, feature requests, or questions:

- Use the appropriate issue template
- Provide clear, detailed descriptions
- Include relevant logs, screenshots, or examples
- Label the issue appropriately

### 2. Work on the Issue

- Comment on the issue to indicate you're working on it
- Create a new branch from `main`:
    ```bash
    git checkout -b feature/your-feature-name
    ```
- Keep commits focused and atomic
- Write clear commit messages

### 3. Submit a Pull Request

- Push your branch to your fork
- Create a pull request with a clear description
- Link to the related issue
- Ensure all CI checks pass

## Code Standards

### Python Code Style

We use several tools to maintain code quality:

- **Black**: Code formatting
- **isort**: Import sorting
- **Flake8**: Linting
- **mypy**: Type checking
- **Bandit**: Security scanning

### Code Formatting

Run the following before committing:

```bash
# Format code
poetry run black supraexporter/
poetry run isort supraexporter/

# Check formatting
poetry run flake8 supraexporter/
poetry run mypy supraexporter/
```

### Naming Conventions

- **Files**: `snake_case.py`
- **Classes**: `PascalCase`
- **Functions/Variables**: `snake_case`
- **Constants**: `UPPER_SNAKE_CASE`
- **Private members**: `_leading_underscore`

### Documentation Standards

- All public functions must have docstrings
- Use Google-style docstrings
- Include type hints for all function parameters and return values
- Add inline comments for complex logic

Example:

```python
def parse_block_height(log_data: str) -> int:
    """Extract the most recent block height from log data.

    Args:
        log_data: Raw log content as a string.

    Returns:
        The latest block height found, or 0 if none found.

    Raises:
        ValueError: If log_data is not a valid string.
    """
    # Implementation here
    pass
```

## Testing

### Test Structure

- Place tests in `supraexporter/tests/`
- Use `test_` prefix for test files
- Group related tests in the same file
- Use descriptive test names

### Running Tests

```bash
# Run all tests
poetry run pytest

# Run with coverage
poetry run pytest --cov=supraexporter

# Run specific test file
poetry run pytest supraexporter/tests/test_validators.py

# Run with verbose output
poetry run pytest -v
```

### Writing Tests

- Use `pytest` framework
- Mock external dependencies
- Test both success and failure cases
- Aim for high test coverage (>80%)

Example test:

```python
def test_parse_block_height_success():
    """Test successful block height parsing."""
    log_data = "Block height: (12345)"
    result = parse_block_height(log_data)
    assert result == 12345

def test_parse_block_height_not_found():
    """Test handling when no block height is found."""
    log_data = "No height information"
    result = parse_block_height(log_data)
    assert result == 0
```

## Documentation

### README Updates

When adding features or changing behavior:

- Update the README.md
- Add new configuration options to the table
- Update examples if necessary
- Keep the documentation current and accurate

### Code Comments

- Comment complex algorithms or business logic
- Explain "why" not just "what"
- Keep comments up-to-date with code changes
- Remove outdated or obvious comments

## Submitting Changes

### Pull Request Guidelines

1. **Title**: Use a clear, descriptive title
2. **Description**: Explain what and why you changed
3. **Testing**: Describe how you tested the changes
4. **Breaking Changes**: Highlight any breaking changes
5. **Related Issues**: Link to relevant issues

### PR Template

```markdown
## Description

Brief description of changes

## Type of Change

- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing

- [ ] Tests pass locally
- [ ] Added tests for new functionality
- [ ] Manual testing completed

## Checklist

- [ ] Code follows project style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No breaking changes (or properly documented)
```

### Review Process

1. **Automated Checks**: All CI checks must pass
2. **Code Review**: At least one maintainer review required
3. **Testing**: Changes must be tested appropriately
4. **Documentation**: Updates must include relevant documentation

### Merge Requirements

- All CI checks passing
- At least one approval from a maintainer
- No unresolved review comments
- Up-to-date with main branch

## Release Process

Releases are handled by maintainers following semantic versioning:

- **Patch** (x.x.1): Bug fixes
- **Minor** (x.1.x): New features (backward compatible)
- **Major** (1.x.x): Breaking changes

## Getting Help

If you need help or have questions:

1. Check the [documentation](README.md)
2. Search existing [issues](https://github.com/blocksize-capital-gmbh/supra-blockchain-metrics-exporter/issues)
3. Open a new issue with the "question" label
4. Join project discussions

## Recognition

Contributors are recognized in several ways:

- Listed in the project contributors
- Mentioned in release notes for significant contributions
- Invited to join the project as a maintainer for sustained contributions

Thank you for contributing to the Supra Blockchain Metrics Exporter! 🚀
