import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import re
from wordcloud import WordCloud

# 1. Baca file CSV ke dalam DataFrame
df = pd.read_csv("tweet_output.csv", names=["Tweet"])

# 2. Gabungkan semua tweet jadi satu string
all_tweets = " ".join(df["Tweet"].astype(str))  # Pastikan semuanya string

# 3. Ekstrak semua hashtag dengan regex
hashtags = re.findall(r"#\w+", all_tweets.lower())

# 4. Hitung frekuensi hashtag
hashtag_counts = Counter(hashtags)

# 5. Ambil 10 hashtag terpopuler
most_common = hashtag_counts.most_common(10)

# 6. Visualisasi dalam bar chart
labels, values = zip(*most_common)

plt.figure(figsize=(10, 5))
plt.bar(labels, values, color='skyblue')
plt.title("10 Hashtag Terpopuler")
plt.xlabel("Hashtag")
plt.ylabel("Jumlah")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 7. WordCloud dari semua tweet
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_tweets)

plt.figure(figsize=(10, 6))
plt.bar(labels, values, color="skyblue")
plt.title("10 Hashtag Terpopuler")
plt.xlabel("Hashtag")
plt.ylabel("Jumlah")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

# 👉 SIMPAN GAMBAR sebelum plt.show()
plt.savefig("top_10_hashtag.png")

plt.show()

