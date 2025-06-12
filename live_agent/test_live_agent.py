#!/usr/bin/env python3
"""Simple test script to demonstrate the live agent."""

import subprocess
import time

print("Testing the live agent...")
print("-" * 50)

# Start the live agent process
process = subprocess.Popen(
    ["uv", "run", "poe", "run-live"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
    bufsize=1,
)

# Give it time to start
time.sleep(2)

# Send a test message
test_message = "Hello! Can you tell me about yourself?\n"
print(f"Sending: {test_message.strip()}")
if process.stdin:
    process.stdin.write(test_message)
    process.stdin.flush()

# Wait a bit for response
time.sleep(3)

# Send exit command
if process.stdin:
    process.stdin.write("exit\n")
    process.stdin.flush()

# Get output
output, errors = process.communicate(timeout=5)
print("\nAgent Output:")
print(output)

if errors:
    print("\nErrors:")
    print(errors)
