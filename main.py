from dotenv import load_dotenv
import os
import pandas as pd 

load_dotenv()

csv_data_path = os.path.join("data", "WorldPopulation2023.csv")
population_df = pd.read_csv(csv_data_path)

print(population_df.head(5))