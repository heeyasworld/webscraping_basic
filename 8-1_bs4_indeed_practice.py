import requests
from bs4 import BeautifulSoup

url = "https://www.indeed.com/jobs?q=front%20end%20developer&l=California&limit=50"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

jobs = soup.find_all("a", {"class": "tapItem"})

for job in jobs:
    link = "https://www.indeed.com" + job["href"]
    title = job.find("span").get_text()
    print("✅", title, link)
