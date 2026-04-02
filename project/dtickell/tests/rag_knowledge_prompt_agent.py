import os
import sys
import glob
from pathlib import Path
from dotenv import load_dotenv

sys.path.append(str(Path(__file__).parent.parent))
from workflow_agents.base_agents import RAGKnowledgePromptAgent

load_dotenv()
openai_api_key = os.environ.get("OPENAI_API_KEY")

# 1. Define Agent Configuration (using the Email Router Product Spec as the embedding)
persona = "You are an expert on the Email Router product specification. Your goal is to provide accurate information based on the provided documentation."

# 2. read in the product spec
product_spec_path = Path(__file__).parent / "Product-Spec-Email-Router.txt"
try:
    with open(product_spec_path, "r") as f:
        knowledge_corpus = f.read()
except FileNotFoundError:
    print(f"Error: {product_spec_path} not found.")
    sys.exit(1)

# 3. Instantiate the RAG Agent
rag_agent = RAGKnowledgePromptAgent(
    openai_api_key=openai_api_key,
    persona=persona,
    chunk_size=500,
    chunk_overlap=0
)

# 4. Process the Knowledge
print(f"Loading knowledge from {product_spec_path}...")
print("Chunking knowledge...")
rag_agent.chunk_text(knowledge_corpus)

print("Calculating embeddings (this may take a moment)...")
rag_agent.calculate_embeddings()

# 5. Test the Agent with some prompts
query = "What are the primary objectives of the Email Router and what is the target for reducing response time? and explain where you got this information"
print(f"\nQuerying Agent with: {query}")
response = rag_agent.find_prompt_in_knowledge(query)
print("\n--- Agent Response #1 ---")
print(response)

query = "What else does the Email Router need to factor in as a product? and explain where you got this information"
print(f"\nQuerying Agent with: {query}")
response = rag_agent.find_prompt_in_knowledge(query)
print("\n--- Agent Response #2 ---")
print(response)

# 6. Cleanup (The agent creates files starting with chunks- and embeddings-)
print("\nCleaning up temporary files...")
files_to_remove = glob.glob("chunks-*.csv") + glob.glob("embeddings-*.csv")
for f in files_to_remove:
    try:
        os.remove(f)
    except OSError as e:
        print(f"Error deleting {f}: {e}")

print("Done.")