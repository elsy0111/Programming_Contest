import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_boston

dataset = load_boston()

print(dataset)

x = dataset.data
t = dataset.target

columns = dataset.feature_names

print(type(x),x.shape)
print(type(t),t.shape)
print(columns)

df = pd.DataFrame(x,columns=columns)
df["terget"] = t

print(df.head())

t = df["terget"].values

x = df.drop(labels=["terget"],axis=1).values

print("t",t)
print("x",x)

 