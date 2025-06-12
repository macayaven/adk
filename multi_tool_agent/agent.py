"""Simple agent that can answer questions about the time and weather in a city."""

import datetime
import os
from pathlib import Path
from zoneinfo import ZoneInfo

from dotenv import load_dotenv
from google.adk.agents import Agent

# Load environment variables from .env file
env_path = Path(__file__).parent / ".env"
load_dotenv(env_path)

# Print the model being used
model_name = os.getenv("GEMINI_MODEL", "Not set")
print(f"Multi-tool agent using model: {model_name}")

# Check if API key is available
if not os.getenv("GOOGLE_API_KEY"):
    print("Warning: GOOGLE_API_KEY not set. Agent may not function properly.")


def get_weather(city: str) -> dict[str, str]:
    """Retrieves the current weather report for a specified city.

    Args:
        city (str): The name of the city for which to retrieve the weather report.

    Returns:
        dict: status and result or error msg.
    """
    if city.lower() == "new york":
        return {
            "status": "success",
            "report": (
                "The weather in New York is sunny with a temperature of 25 degrees"
                " Celsius (77 degrees Fahrenheit)."
            ),
        }
    return {
        "status": "error",
        "error_message": f"Weather information for '{city}' is not available.",
    }


def get_current_time(city: str) -> dict[str, str]:
    """Returns the current time in a specified city.

    Args:
        city (str): The name of the city for which to retrieve the current time.

    Returns:
        dict: status and result or error msg.
    """
    if city.lower() == "new york":
        tz_identifier = "America/New_York"
    else:
        return {
            "status": "error",
            "error_message": (f"Sorry, I don't have timezone information for {city}."),
        }

    tz = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(tz)
    report = f"The current time in {city} is {now.strftime('%Y-%m-%d %H:%M:%S %Z%z')}"
    return {"status": "success", "report": report}


root_agent = Agent(
    name="weather_time_agent",
    model=os.getenv("GEMINI_MODEL", "gemini-1.5-pro-latest"),
    description=("Agent to answer questions about the time and weather in a city."),
    instruction=(
        "You are a helpful agent who can answer user questions about the time "
        "and weather in a city."
    ),
    tools=[get_weather, get_current_time],
)
