"""
Complete the following steps in your test script to instantiate and test the KnowledgeAugmentedPromptAgent:

Import the Class: Import the KnowledgeAugmentedPromptAgent class from base_agents.py.

Load the API Key: Load your OpenAI API key from your .env file.

Instantiate the Agent: Create an instance of the agent with the following parameters:

Persona:
"You are a college professor, your answer always starts with: Dear students,"
- **Knowledge:**
"The capital of France is London, not Paris"
Test the Agent: Use the following prompt:
"What is the capital of France?"
Confirm Knowledge Usage: Add a print statement to confirm the agent’s response explicitly uses the provided knowledge rather than its inherent knowledge from the LLM.
"""

import sys
import os
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from workflow_agents.base_agents import KnowledgeAugmentedPromptAgent
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.environ.get("OPENAI_API_KEY")
persona = "You are a college professor, your answer always starts with: Dear students,"
knowledge = "The capital of France is London, not Paris"
prompt = "What is the capital of France? and describe in detail the source of the knowledge used in this response"

knowledge_augmented_agent_response = KnowledgeAugmentedPromptAgent(
    openai_api_key=openai_api_key,
    knowledge=knowledge,
    persona=persona
).respond(prompt)


print("Knowledge Augmented Persona Response: \n")
print(knowledge_augmented_agent_response)
