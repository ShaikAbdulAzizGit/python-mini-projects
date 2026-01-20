import requests
from secret_key import api_key
key=api_key
query=input("What topic are you intrested today ?....")

url=f"https://newsapi.org/v2/everything?q={query}&from=2025-05-19&to=2025-05-19&sortBy=popularity&apiKey={key}"

r=requests.get(url)
data=r.json()

articles=data["articles"]

for index,article in enumerate(articles):
    print(f"{index+1} .Title:{article["title"]}\nDescription:{article["description"]}\nurl:{article["url"]}")
    print("\n\n***********************************\n\n")
