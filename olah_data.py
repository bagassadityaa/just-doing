import json
import pandas as pd
import re

# Buka file JSON
with open("hasil_tweet.json", "r", encoding="utf-8") as f:
    tweets = json.load(f)

# Masukkan ke DataFrame
df = pd.DataFrame(tweets, columns=["text"])

# Bersihkan teks
def clean_text(text):
    text = re.sub(r"http\S+", "", text)       # hapus URL
    text = re.sub(r"#\S+", "", text)          # hapus hashtag
    text = re.sub(r"@\S+", "", text)          # hapus mention
    text = re.sub(r"\n", " ", text)           # newline jadi spasi
    text = text.lower().strip()
    return text

df["cleaned"] = df["text"].apply(clean_text)

# Tampilkan hasil
print(df[["text", "cleaned"]].head())

# Simpan hasil bersih
df.to_csv("tweet_bersih.csv", index=False, encoding="utf-8")
