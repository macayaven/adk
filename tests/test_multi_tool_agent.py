"""Tests for multi_tool_agent."""

from multi_tool_agent.agent import get_current_time, get_weather


def test_get_weather() -> None:
    """Test weather function returns expected format."""
    # Test valid city
    result = get_weather("New York")
    assert result["status"] == "success"
    assert "report" in result
    assert "sunny" in result["report"]
    assert "25 degrees" in result["report"]

    # Test with different case
    result = get_weather("new york")
    assert result["status"] == "success"

    # Test unknown city
    result = get_weather("Unknown City")
    assert result["status"] == "error"
    assert "error_message" in result


def test_get_current_time() -> None:
    """Test time function returns expected format."""
    # Test valid city (New York)
    result = get_current_time("New York")
    assert result["status"] == "success"
    assert "report" in result
    assert "current time" in result["report"]
    assert "New York" in result["report"]

    # Test with lowercase
    result = get_current_time("new york")
    assert result["status"] == "success"

    # Test invalid city
    result = get_current_time("Invalid City")
    assert result["status"] == "error"
    assert "error_message" in result
