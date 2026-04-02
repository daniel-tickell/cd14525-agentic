"""
Complete the following tasks in your test script to test the AugmentedPromptAgent:

Import the Class: Import the AugmentedPromptAgent class from base_agents.py.

Instantiate the Agent: Create an instance of the AugmentedPromptAgent class using your OpenAI API key and a defined persona.

Send a Prompt: Send a prompt to the agent and store the result in a variable named augmented_agent_response.

Print the Response: Clearly print the augmented_agent_response to verify the agent’s behavior.

Provide Explanatory Comments: Include comments discussing:

The type of knowledge the agent likely used to generate its response.
How specifying the agent’s persona affected the final output.
"""
import sys
import os
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from workflow_agents.base_agents import AugmentedPromptAgent
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.environ.get("OPENAI_API_KEY")
base_persona = "You are a unhelpful assistant."
expanded_persona = "You are a helpful assistant. who explains things in a fun (in pirate speak) and engaging way and loves explaining more about the topic"

prompt = "What is the Capital of France?"

base_augmented_agent_response = AugmentedPromptAgent(
    openai_api_key=openai_api_key,
    persona=base_persona
).respond(prompt)

expanded_augmented_agent_response = AugmentedPromptAgent(
    openai_api_key=openai_api_key,  
    persona=expanded_persona
).respond(prompt)

print("base Persona Response: \n")
print(base_augmented_agent_response)
print("\nexpanded Persona Response: \n")
print(expanded_augmented_agent_response)
