# ADK Learning Project Configuration

## Project Overview
This is a learning project for the Google Agent Development Kit (ADK) with multiple agent implementations, comprehensive testing, and CI/CD setup.

## Essential Information
- **Package Manager**: `uv` (v0.4.18 or higher)
- **Task Runner**: `poe` (poethepoet)
- **Python Version**: 3.13
- **ADK Package**: `google-adk>=1.3.0`
- **Primary Model**: Gemini 2.0 Flash

## Project Structure
```
adk-1/
├── multi_tool_agent/      # Main agent with weather/time tools
│   ├── agent.py          # Agent implementation
│   └── .env             # Environment variables
├── agent_team/           # Agent team tutorial implementation
│   ├── agent_team.ipynb # Jupyter notebook tutorial
│   ├── tools.py         # Extracted tools for testing
│   └── .env             # Environment variables
├── live_agent/           # Live interactive agent
│   ├── agent.py         # Stream-based agent
│   └── test_live_agent.py
├── tests/                # Test suite
│   ├── test_multi_tool_agent.py
│   └── test_agent_team.py
├── .github/workflows/    # CI/CD
│   └── code-quality.yml # GitHub Actions workflow
├── pyproject.toml       # All configurations
├── .pre-commit-config.yaml
└── CLAUDE.md            # This file
```

## CRITICAL: Always Run Before Committing
```bash
# Run ALL quality checks (format, lint, typecheck)
uv run poe check

# If checks fail, auto-fix what's possible
uv run poe fix

# Run tests
uv run poe test
```

## Complete Task Reference
| Command | Purpose | Details |
|---------|---------|---------|
| **Quality Checks** |
| `uv run poe check` | Run ALL checks | format-check + lint + typecheck |
| `uv run poe fix` | Auto-fix issues | format + lint-fix |
| `uv run poe all` | Fix + typecheck | fix + typecheck |
| **Individual Tools** |
| `uv run poe lint` | Linting only | ruff check . |
| `uv run poe lint-fix` | Fix linting | ruff check . --fix |
| `uv run poe format` | Format code | black . |
| `uv run poe format-check` | Check formatting | black --check . |
| `uv run poe typecheck` | Type checking | mypy . |
| **Testing** |
| `uv run poe test` | Run tests | pytest -v tests/ |
| **Running Agents** |
| `uv run poe run` | Run multi_tool_agent | adk run multi_tool_agent |
| `uv run poe run-multi` | Run multi_tool_agent | adk run multi_tool_agent |
| `uv run poe run-live` | Run live_agent | adk run live_agent |
| `uv run poe web` | Web UI for multi_tool | adk web multi_tool_agent |
| `uv run poe notebook` | Start Jupyter | jupyter notebook |

## Environment Configuration
### Required Environment Variables
- `GOOGLE_API_KEY` - Required for all agents
- `OPENAI_API_KEY` - Optional for multi-model support
- `ANTHROPIC_API_KEY` - Optional for multi-model support

### Environment Files
- `multi_tool_agent/.env` - Main agent configuration
- `agent_team/.env` - Agent team configuration
- `live_agent/.env` - Live agent configuration (if needed)

## Code Quality Configuration
### Tools and Standards
- **Formatter**: Black (line length: 88)
- **Linter**: Ruff (extensive rule set)
- **Type Checker**: mypy (strict mode)
- **Pre-commit**: Configured with all tools
- **CI/CD**: GitHub Actions on push/PR

### Special Rules
- **Notebooks** (`*.ipynb`): Relaxed linting rules (allows prints, long lines, etc.)
- **Test files** (`test_*.py`): Print statements allowed
- **Agent files**: Print statements allowed for demo purposes

### Import Notes
- ADK imports: `from google.adk import Agent, Runner`
- Tools import: `from google.adk.tools import ToolContext`
- Models: `from google.adk.models import LiteLlm`
- For notebooks in `agent_team/`: Uses simplified imports shown in tutorial

## Testing
- **Framework**: pytest
- **Location**: `tests/` directory
- **Coverage**: Basic functionality tests for all agents
- **Mocking**: Uses mock objects for ToolContext in tests

## GitHub Actions
- **Workflow**: `.github/workflows/code-quality.yml`
- **Jobs**: code-quality, pre-commit, test
- **Python**: 3.13
- **Triggers**: Push to main/develop, PRs

## Common Issues and Solutions
1. **Import errors with ADK**:
   - Use `google.adk` not just `adk`
   - ToolContext is in `google.adk.tools`

2. **Notebook linting errors**:
   - Already configured to ignore common notebook patterns
   - Jupyter notebooks have relaxed rules

3. **Type checking errors**:
   - Use `# type: ignore` for mock objects in tests
   - Add type annotations to all functions

## Development Workflow
1. Make changes
2. Run `uv run poe fix` to auto-format
3. Run `uv run poe check` to verify all quality checks
4. Run `uv run poe test` to ensure tests pass
5. Commit with descriptive message

## Next Steps and Improvements
- Expand test coverage as new features are added
- Add more specialized agents to the team
- Implement integration tests
- Add documentation for each agent type
- Create more comprehensive examples
