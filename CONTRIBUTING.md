# Contributing to Ell Adventure

We're excited that you're interested in contributing to Ell Adventure! This document outlines the process for contributing to this project and how to get started.

## Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [Getting Started](#getting-started)
3. [How to Contribute](#how-to-contribute)
4. [Reporting Bugs](#reporting-bugs)
5. [Suggesting Enhancements](#suggesting-enhancements)
6. [Pull Request Process](#pull-request-process)
7. [Style Guidelines](#style-guidelines)
8. [Additional Notes](#additional-notes)

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior to [project_email@example.com].

## Getting Started

1. Fork the repository on GitHub.
2. Clone your fork locally:
   ```bash
   git clone https://github.com/Nitewriter/ell-adventure.git
   cd ell-adventure
   ```
3. Set up your development environment as described in the README.md file.
4. Create a branch for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## How to Contribute

1. Ensure your code adheres to the project's style guidelines and best practices.
2. Make your changes and commit them with a clear, descriptive commit message.
3. Push your changes to your fork on GitHub.
4. Submit a pull request to the main repository.

## Reporting Bugs

1. Check the GitHub Issues to see if the bug has already been reported.
2. If not, create a new issue, providing a clear title and description.
3. Include as much relevant information as possible, and steps to reproduce the issue.

## Suggesting Enhancements

1. Check the GitHub Issues to see if the enhancement has already been suggested.
2. If not, create a new issue, clearly describing the enhancement and its potential benefits.

## Pull Request Process

1. Ensure your code follows the style guidelines of this project.
2. Update the README.md with details of changes, if applicable.
3. Your pull request will be reviewed by maintainers, who may request changes or provide feedback.
4. Once approved, your pull request will be merged.

## Style Guidelines

- Follow PEP 8 style guide for Python code.
- Use type hints as per Python 3.12+ standards.
- Write clear, descriptive commit messages.
- Add docstrings to all functions, classes, and modules.
- Use f-strings for string interpolation.
- For UI components, use the Textual library.

## Additional Notes

- Please note that this project uses Poetry for dependency management. Make sure to update `pyproject.toml` if you add or modify dependencies.
- Run tests using `make test` before submitting your pull request.
- Use `make lint` and `make format` to ensure your code meets our style guidelines.

Thank you for contributing to Ell Adventure!
