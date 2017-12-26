import pandas as pd

label = pd.read_csv("labeled.csv")
sample = label.sample(n=500)
sample_2 = label.drop(sample.index.values)

print(sample_2)
