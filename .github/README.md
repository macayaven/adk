# GitHub Actions Workflows

This directory contains GitHub Actions workflows for continuous integration.

## Code Quality Workflow (`code-quality.yml`)

This workflow runs on every push and pull request to ensure code quality. It includes:

### Jobs

1. **code-quality**: Runs formatting, linting, and type checking
   - Uses `uv` for dependency management
   - Runs `poe format-check` to verify code formatting
   - Runs `poe lint` for linting with Ruff
   - Runs `poe typecheck` for type checking with mypy
   - Runs `poe check` as a final combined check

2. **pre-commit**: Runs all pre-commit hooks
   - Ensures consistency with local development

3. **test**: Runs the test suite
   - Uses pytest to run all tests in the `tests/` directory
   - Can use `GOOGLE_API_KEY` from GitHub secrets if needed

### Configuration

- Python version: 3.13
- Runs on: ubuntu-latest
- Triggers: Push to main/develop, Pull requests to main/develop

### Secrets Required

- `GOOGLE_API_KEY` (optional): For tests that require Google API access

## Local Development

To ensure your code passes CI checks, run these commands locally:

```bash
# Run all checks (format, lint, typecheck)
uv run poe check

# Run tests
uv run poe test

# Fix auto-fixable issues
uv run poe fix

# Run pre-commit hooks
pre-commit run --all-files
```