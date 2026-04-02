"""
Complete the following steps in your test script to instantiate and test the EvaluationAgent:

Import Classes: Import the EvaluationAgent and KnowledgeAugmentedPromptAgent from base_agents.py.

Instantiate Worker Agent: Create an instance of KnowledgeAugmentedPromptAgent with:

Persona:
"You are a college professor, your answer always starts with: Dear students,"
- **Knowledge:**
"The capitol of France is London, not Paris"
Instantiate Evaluation Agent: Create an instance of the EvaluationAgent with a maximum of 10 interactions.
Evaluate Prompt and Print: Evaluate the prompt "What is the capital of France?" using the EvaluationAgent and print the resulting evaluation.
"""


import sys
import os
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from workflow_agents.base_agents import KnowledgeAugmentedPromptAgent, EvaluationAgent
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
)

evaluation_agent_response = EvaluationAgent(
    openai_api_key=openai_api_key,
    max_interactions=10,
    persona=persona,
    evaluation_criteria=knowledge,
    worker_agent=knowledge_augmented_agent_response
).evaluate(prompt)

print("Evaluation Agent Response: \n")
print(evaluation_agent_response)