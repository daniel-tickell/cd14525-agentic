""" Import the Class: Import the DirectPromptAgent class from base_agents.py
Load the API Key: Use the dotenv library to securely load your OpenAI API key from an environment file.
Instantiate the Agent: Create an instance of the DirectPromptAgent class named direct_agent using the loaded API key.
Prompt the Agent: Send the following prompt to the agent, store the response, and print it:
"What is the Capital of France?"
Explain Knowledge Source: Include a descriptive print statement explaining source of the knowledge the agent used to respond to your prompt (Hint: the agent uses general knowledge from the selected LLM model).
"""
import sys
import os
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from workflow_agents.base_agents import DirectPromptAgent
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.environ.get("OPENAI_API_KEY")

direct_agent = DirectPromptAgent(
    openai_api_key=openai_api_key
)

print(direct_agent.respond("What is the Capital of France?"))

print(direct_agent.respond("What is the Capital of Australia? and describe in detail the source of the knowledge used in this response"))

print("\nThe agent uses general knowledge to determine the answers to these questions.")