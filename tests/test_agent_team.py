"""Tests for agent team components."""

from agent_team.tools import get_preference, get_weather, save_preference


def test_agent_team_weather() -> None:
    """Test the weather tool from agent team."""
    # Test known cities
    result = get_weather("New York")
    assert result["status"] == "success"
    assert "sunny" in result["report"]
    assert "25°C" in result["report"]

    result = get_weather("London")
    assert result["status"] == "success"
    assert "cloudy" in result["report"]
    assert "15°C" in result["report"]

    result = get_weather("Tokyo")
    assert result["status"] == "success"
    assert "rain" in result["report"]
    assert "18°C" in result["report"]

    # Test unknown city
    result = get_weather("Atlantis")
    assert result["status"] == "error"
    assert "error_message" in result
    assert "Atlantis" in result["error_message"]

    # Test case insensitivity
    result = get_weather("NEW YORK")
    assert result["status"] == "success"

    # Test with spaces
    result = get_weather("New  York")
    assert result["status"] == "success"


def test_session_state_tools() -> None:
    """Test tools that use session state."""

    # Create a mock context with session_state attribute
    class MockContext:
        def __init__(self) -> None:
            self.session_state: dict[str, str] = {}

    context = MockContext()

    # Test saving preference
    result = save_preference(context, "color", "blue")
    assert "Preference saved" in result
    assert context.session_state["color"] == "blue"

    # Test getting preference
    result = get_preference(context, "color")
    assert "blue" in result

    # Test getting non-existent preference
    result = get_preference(context, "nonexistent")
    assert "No preference set" in result
