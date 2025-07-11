import requests
from bs4 import BeautifulSoup
import csv

url = "https://news.yahoo.co.jp/"
res = requests.get(url)
res.encoding = res.apparent_encoding
soup = BeautifulSoup(res.text, "html.parser")

headlines = soup.select("a[href*='/articles/']")

#重複除去のためにセット化
titles_urls = set()

for h in headlines:
    title = h.text.strip()
    link = h.get("href")
    if title and link and len(title) > 5:
        titles_urls.add((title, link))

#csvに書き出し
with open("news.csv", "w", newline="",encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["見出し","url"])
    for title  , link in list(titles_urls)[:10]:
        writer.writerow([title, link])