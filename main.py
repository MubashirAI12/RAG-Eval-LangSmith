import os
from dotenv import load_dotenv 
from config import *
from utils.dataset import create_dataset
load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("openai_key")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("langsmith_api_key")


def main():
    if is_dataset_creation:
        create_dataset(dataset_name="law_co-testing")
    
    return True

if __name__ == "__main__":
    main()