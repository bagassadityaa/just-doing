import pandas as pd

# Membaca file CSV
df = pd.read_csv("tweet_output.csv", names=["Tweet"])

# Menampilkan 10 tweet pertama
print(df.head(10))
