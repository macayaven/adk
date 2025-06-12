"""Live agent for real-time interactions with Gemini models."""

import os
from pathlib import Path
from typing import Any

from dotenv import load_dotenv
from google.adk.agents import Agent

# First try to load from local .env, then from parent directory
env_path = Path(__file__).parent / ".env"
if not env_path.exists():
    env_path = Path(__file__).parent.parent / "multi_tool_agent" / ".env"
load_dotenv(env_path)

# Print the model being used (if configured)
model_name = os.getenv("GEMINI_MODEL", "gemini-2.0-flash-live-001")
print(f"Live agent using model: {model_name}")

# Check if API key is available
if not os.getenv("GOOGLE_API_KEY"):
    print("Warning: GOOGLE_API_KEY not set. Agent may not function properly.")


def echo_response(message: str) -> str:
    """Simple echo function for testing live interactions.

    Args:
        message: The message to echo back

    Returns:
        The echoed message with a prefix
    """
    return f"Live agent received: {message}"


def get_system_info() -> dict[str, Any]:
    """Get system information for the live agent.

    Returns:
        Dictionary containing system information
    """
    return {
        "agent_type": "live",
        "model": model_name,
        "status": "operational",
        "capabilities": ["real-time chat", "streaming responses", "voice interaction"],
    }


# Create the root agent for live interactions
root_agent = Agent(
    name="live_assistant",
    model=model_name,
    description="A live assistant for real-time interactions and streaming responses",
    instruction=(
        "You are a helpful live assistant that can engage in real-time conversations. "
        "You can respond to user queries immediately and provide streaming responses. "
        "Be conversational, friendly, and helpful."
    ),
    tools=[echo_response, get_system_info],
)
