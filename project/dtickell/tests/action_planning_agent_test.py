"""
Complete the following steps in your test script to test the ActionPlanningAgent:

Import Libraries and Class: Import necessary libraries (e.g., dotenv) and the ActionPlanningAgent class from base_agents.py.
Load API Key: Load environment variables and assign your OpenAI API key to a variable, for example, openai_api_key.
Instantiate the Agent: Create an instance of the ActionPlanningAgent, providing it with the defined knowledge (if any is specifically required for its action planning task beyond general instruction) and the API key.
Verify Functionality: Test the agent by sending it the following prompt and printing the extracted action steps:
"One morning I wanted to have scrambled eggs"
"""
import sys
import os
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from workflow_agents.base_agents import ActionPlanningAgent
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.environ.get("OPENAI_API_KEY")
knowledge = """
    Scrambled Eggs requires 2 eggs, milk, butter, salt, and pepper. 
    It takes 5 minutes to cook. 
    You must whisk the eggs and milk together before cooking. 
    You must heat the butter in a pan over medium heat. 
    You must pour the egg mixture into the pan and cook until set. 
    You must season with salt and pepper.
    Morning is the time between sunrise and noon. """

action_planning_agent = ActionPlanningAgent(
    openai_api_key=openai_api_key,
    knowledge=knowledge
)

print(action_planning_agent.extract_steps_from_prompt("One morning I wanted to have scrambled eggs"))

print("\nThe agent is using the specific knowledge provided in the prompt, the steps included are verbatim from the knowledge I provided."