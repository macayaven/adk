"""Tools for the agent team."""

from typing import Any, Protocol


class ContextWithState(Protocol):
    """Protocol for context objects with session state."""

    session_state: dict[str, Any]


def get_weather(city: str) -> dict[str, str]:
    """Retrieves the current weather report for a specified city."""
    city_normalized = city.lower().replace(" ", "")

    # Mock weather database
    mock_weather_db = {
        "newyork": {
            "status": "success",
            "report": "The weather in New York is sunny with a temperature of 25°C.",
        },
        "london": {
            "status": "success",
            "report": "It's cloudy in London with a temperature of 15°C.",
        },
        "tokyo": {
            "status": "success",
            "report": "Tokyo is experiencing light rain and a temperature of 18°C.",
        },
    }

    if city_normalized in mock_weather_db:
        return mock_weather_db[city_normalized]
    return {
        "status": "error",
        "error_message": f"Sorry, I don't have weather information for '{city}'.",
    }


def save_preference(context: ContextWithState, key: str, value: str) -> str:
    """Saves user preference to session state."""
    context.session_state[key] = value
    return f"Preference saved: {key} = {value}"


def get_preference(context: ContextWithState, key: str) -> str:
    """Retrieves user preference from session state."""
    value = context.session_state.get(key, "No preference set")
    return f"Preference for {key}: {value}"


def get_weather_with_memory(context: ContextWithState, city: str) -> dict[str, str]:
    """Get weather and remember the last queried city."""
    # Save the city as a preference
    context.session_state["last_city"] = city

    # Get weather (reusing our function)
    return get_weather(city)
