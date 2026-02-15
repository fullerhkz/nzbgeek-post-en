# Contributing to NZBGeek Post

Thank you for considering contributing to NZBGeek Post! This document provides guidelines and instructions for contributing to the project.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Pull Request Process](#pull-request-process)
- [Coding Standards](#coding-standards)
- [Commit Messages](#commit-messages)
- [Testing](#testing)

## Code of Conduct

This project adheres to a code of conduct. By participating, you are expected to uphold this code. Please be respectful and constructive in all interactions.

## How Can I Contribute?

### Reporting Bugs

Before creating a bug report, please check existing issues to avoid duplicates.

**When reporting a bug, include:**
- Python version and operating system
- Steps to reproduce the issue
- Expected behavior vs actual behavior
- Screenshots if applicable
- Error messages or logs

### Suggesting Enhancements

Enhancement suggestions are welcome! Please:
- Check if the feature has already been suggested
- Provide a clear description of the feature
- Explain why this feature would be useful
- Include examples of how it would work

### Code Contributions

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes**
4. **Test your changes**
5. **Commit your changes**
6. **Push to your fork**
7. **Open a Pull Request**

## Development Setup

### Prerequisites

- Python 3.7+
- pip
- git

### Setting Up Development Environment

```bash
# Clone your fork
git clone https://github.com/your-username/nzbgeek-post-en.git
cd nzbgeek-post-en

# Install dependencies
pip install -r requirements.txt

# Configure environment variables for testing
# (See README.md for details)
```

### Running Tests

```bash
# Run the script
python nzbgeek-post.py

# Test executable build
python build_exe.py
```

## Pull Request Process

1. **Update Documentation**: If you add/change features, update README.md and CHANGELOG.md
2. **Follow Coding Standards**: Ensure code follows Python PEP 8 style guide
3. **Test Thoroughly**: Test on Windows if possible (primary platform)
4. **Write Clear Commits**: Use descriptive commit messages
5. **Update Version**: If needed, update version in code and CHANGELOG.md
6. **Create PR**: Provide clear description of changes

### PR Checklist

- [ ] Code follows project style guidelines
- [ ] Documentation has been updated
- [ ] CHANGELOG.md has been updated
- [ ] All tests pass
- [ ] No new warnings or errors
- [ ] PR title clearly describes the change

## Coding Standards

### Python Code Style

- Follow [PEP 8](https://pep8.org/) style guide
- Use 4 spaces for indentation (no tabs)
- Maximum line length: 100 characters for code, 80 for docstrings
- Use descriptive variable and function names
- Add type hints for function parameters and returns
- Document functions with docstrings

### Example Code Style

```python
def process_file(file_path: Path, category: str) -> bool:
    """
    Processes an NZB file and submits to NZBGeek
    
    Args:
        file_path: Path to NZB file
        category: Category ID
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Implementation
        return True
    except Exception as e:
        print_colored(f"Error: {e}", Fore.RED)
        return False
```

### UI Text Guidelines

- Use clear, concise English
- Be consistent with existing UI messages
- Use emojis sparingly and appropriately
- Provide helpful error messages with solutions

## Commit Messages

Follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

```
type(scope): brief description

Detailed description if needed

- Change 1
- Change 2
```

### Types

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Maintenance tasks

### Examples

```bash
feat: add support for NFO file submission

- Add NFO file parameter to API call
- Update UI to prompt for NFO file
- Add documentation for NFO usage

fix: correct file path handling on Linux

- Use Path.resolve() for absolute paths
- Fix slash direction issues
- Test on Ubuntu 22.04

docs: update README with Linux installation steps
```

## Testing

### Manual Testing

Test on multiple platforms if possible:
- Windows 10/11
- Linux (Ubuntu, Debian)
- macOS

### Test Cases

1. **Normal Operation**
   - Submit single NZB file
   - Submit multiple NZB files
   - Different categories
   - File movement after submission

2. **Error Handling**
   - Missing API key
   - Invalid folder paths
   - Network errors
   - Invalid NZB files
   - API errors

3. **UI/UX**
   - Colors display correctly
   - Progress bars work
   - Menu navigation
   - Exit options

### Executable Testing

If you modify the main script:

```bash
# Build executable
python build_exe.py

# Test executable
dist\nzbgeek-post.exe  # Windows
./dist/nzbgeek-post    # Linux/Mac
```

## Questions?

Feel free to open an issue with the `question` label if you have any questions about contributing.

---

Thank you for contributing to NZBGeek Post! 🎉
