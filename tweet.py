import tweepy
import json

# Token milikmu
bearer_token = ""

# Koneksi ke API
client = tweepy.Client(bearer_token=bearer_token, wait_on_rate_limit=True)

# Query
query = "#IndonesiaGelap -is:retweet lang:id"

# Ambil tweet lengkap
response = client.search_recent_tweets(
    query=query,
    max_results=100,
    tweet_fields=["created_at", "author_id", "id", "text"]
)

# Simpan hasil dalam list of dictionary
tweets_data = []

for tweet in response.data:
    tweet_dict = {
        "id": tweet.id,
        "author_id": tweet.author_id,
        "created_at": tweet.created_at.isoformat(),
        "text": tweet.text
    }
    tweets_data.append(tweet_dict)

# Simpan ke file JSON
with open("tweet_struktur.json", "w", encoding="utf-8") as f:
    json.dump(tweets_data, f, ensure_ascii=False, indent=2)

print("Data berhasil disimpan dalam format terstruktur!")
