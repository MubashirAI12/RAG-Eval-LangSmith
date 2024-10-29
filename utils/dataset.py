from langsmith import Client
from langsmith.evaluation import evaluate

client = Client()

# Define dataset: these are your test cases
def create_dataset(dataset_name: str):
    try:
        dataset = client.create_dataset(dataset_name, description="A sample dataset related to legal queries")
        client.create_examples(
            inputs=[
                {"postfix": "to LangSmith"},
                {"postfix": "to Evaluations in LangSmith"},
            ],
            outputs=[
                {"output": "Welcome to LangSmith"},
                {"output": "Welcome to Evaluations in LangSmith"},
            ],
            dataset_id=dataset.id,
        )
    except Exception as e:
        print(f"Error: {e}")