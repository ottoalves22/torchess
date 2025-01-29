#download lichess datasets 
import kagglehub
import pandas as pd
# Download latest version
path = kagglehub.dataset_download("datasnaek/chess")

print("Path to dataset files:", path)

dataset_full = pd.read_csv(f"{path}/games.csv")

dataset = dataset_full[["victory_status", "winner", "moves", "opening_name"]]

print(dataset.head())