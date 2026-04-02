"""
Complete the following steps in your test script to instantiate and test the RoutingAgent:

Import Classes: Import KnowledgeAugmentedPromptAgent and RoutingAgent from base_agents.py.

Instantiate Texas Agent: Create an instance of KnowledgeAugmentedPromptAgent for Texas-related knowledge.

Instantiate Europe Agent: Create another instance of KnowledgeAugmentedPromptAgent for Europe-related knowledge.

Instantiate Math Agent: Create a third KnowledgeAugmentedPromptAgent specifically for math-related prompts.

Define Agent Functions/Lambdas: For each agent, define a function or lambda expression that will be called if that agent is selected. These functions will embody the agent's task (e.g., answering Texas-related questions).

Assign Agents to Router: Assign these agents (along with their descriptions and callable functions/lambdas) to the agents attribute of the RoutingAgent instance.

Test Routing with Prompts: Test your routing agent with the following prompts and print the results:

"Tell me about the history of Rome, Texas"
"Tell me about the history of Rome, Italy"
"One story takes 2 days, and there are 20 stories"
"""
import sys
import os
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from workflow_agents.base_agents import KnowledgeAugmentedPromptAgent, RoutingAgent, DirectPromptAgent
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.environ.get("OPENAI_API_KEY")

direct_agent = DirectPromptAgent(
    openai_api_key=openai_api_key
)




texas_agent = KnowledgeAugmentedPromptAgent(
    openai_api_key=openai_api_key,
    knowledge=direct_agent.respond("top 100 facts about Texas"),
    persona="You are a travel Agent from Texas with indept knowledge of Texas"
)

europe_agent = KnowledgeAugmentedPromptAgent(
    openai_api_key=openai_api_key,
    knowledge=direct_agent.respond("top 100 facts about Europe"),
    persona="You are a travel Agent from Europe with indept knowledge of Europe"
)

math_agent = KnowledgeAugmentedPromptAgent(
    openai_api_key=openai_api_key,
    knowledge=direct_agent.respond("fundamentals of math"),
    persona="You are a math professor with indept knowledge of math"
)

def texas_agent_function(prompt):
    return texas_agent.respond(prompt)

def europe_agent_function(prompt):
    return europe_agent.respond(prompt)

def math_agent_function(prompt):
    return math_agent.respond(prompt)

routing_agent = RoutingAgent(
    openai_api_key=openai_api_key,
    agents=[
        {"name": "texas", "description": "Texas-related knowledge", "func": texas_agent_function},
        {"name": "europe", "description": "Europe-related knowledge", "func": europe_agent_function},
        {"name": "math", "description": "Math-related knowledge", "func": math_agent_function}
    ]
)   

print(routing_agent.route("Tell me about the history of Rome, Texas"))
print(routing_agent.route("Tell me about the history of Rome, Italy"))
print(routing_agent.route("One story takes 2 days, and there are 20 stories"))
