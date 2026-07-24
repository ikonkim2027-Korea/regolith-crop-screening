import pandas as pd

df = pd.read_csv("data/raw/gasteiner/Dataset_All.csv", sep=";")
print(df.shape)
print(df.columns.tolist())

psd = pd.read_csv("data/raw/gasteiner/Dataset_Samples_PSD.csv", sep=";")
print(psd.head())
