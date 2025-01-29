#download lichess datasets 
import sklearn.preprocessing
import kagglehub
import pandas as pd
import sklearn

# Download latest version
path = kagglehub.dataset_download("datasnaek/chess")

print("Path to dataset files:", path)

dataset_full = pd.read_csv(f"{path}/games.csv")

dataset = dataset_full[["victory_status", "winner", "moves", "opening_name"]]

dataset_filtered = dataset.loc[dataset["victory_status"] !=  "outoftime", ["victory_status", "winner", "moves", "opening_name"]]

#cria as labels para os nomes de abertura. COloquei em outro dataframe pra ter como desfazer as labels depois...
dataset_filtered["opening_name"] = sklearn.preprocessing.LabelEncoder().fit_transform(dataset_filtered["opening_name"])

print(dataset)
