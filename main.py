from dotenv import load_dotenv
import os
import pandas as pd 
from prompts import new_prompt, instruction_str
import google.generativeai as genai

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)


csv_data_path = os.path.join("data", "WorldPopulation2023.csv")
population_df = pd.read_csv(csv_data_path)


def generate_pandas_code(query, df):
    "code generation"
    df_str = df.head().to_string()
    prompt_text = new_prompt.format(df_str=df_str, instruction_str=instruction_str, query_str=query)
    
    prompt_text = prompt_text.replace("df", "population_df") 
    print(f"Prompt text: \n{prompt_text}\n")
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt_text)
    
    return response.text.strip()


def query_population(query):
   
    code = generate_pandas_code(query, population_df)
    
    print(f"Generated code: {code}")
    
    try:
        local_vars = {"population_df": population_df}
        exec(f"result = {code}", {}, local_vars)
        return local_vars.get("result", "No result").item()
    except Exception as e:
        return f"Error executing code: {str(e)}"


query = "What is the population of Zambia?"
result = query_population(query)

print(f"Query result: {result}")
