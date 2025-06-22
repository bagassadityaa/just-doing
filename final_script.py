import json
import pandas as pd

# Baca data dari file JSON
with open("hasil_tweet.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Karena isi JSON sudah berupa list of string (tweet), kita bisa langsung pakai
tweets = [tweet.strip() for tweet in data]  # ini opsional

# Simpan ke DataFrame dan CSV
df = pd.DataFrame(tweets, columns=["tweet"])
df.to_csv("tweet_output.csv", index=False, encoding="utf-8-sig")

print("Berhasil disimpan ke tweet_output.csv")
