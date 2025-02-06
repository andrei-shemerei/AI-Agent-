from dotenv import load_dotenv
import os
import pandas as pd 
from llama_index.llms.gemini import Gemini
from llama_index.core import Settings
from llama_index.experimental.query_engine import PandasQueryEngine
from prompts import new_prompt, instruction_str, context
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from note_engine import note_engine
#import google.generativeai as genai

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
#genai.configure(api_key=GOOGLE_API_KEY)

llm = Gemini()
Settings.llm = llm

csv_data_path = os.path.join("data", "WorldPopulation2023.csv")
population_df = pd.read_csv(csv_data_path)

population_query_engine = PandasQueryEngine(
    df=population_df, verbose=True, instruction_str=instruction_str
)

population_query_engine.update_prompts({"pandas_prompt" : new_prompt})

tools = [
    QueryEngineTool(
        query_engine=population_query_engine,
        metadata=ToolMetadata(
            name="population_data",
            description="this gives information at the world population and demographics",
        ),
    ),
    note_engine
]

agent = ReActAgent.from_tools(
    tools=tools,
    llm=llm,
    verbose=True,
    context=context,
)


while True:
    prompt = input("Enter a prompt (or tupe 'q' to exit): ")
    if prompt == "q":
        print("Programm is existing")
        break

    result = agent.query(prompt)
    print(result)
    
