import requests
from bs4 import BeautifulSoup


url = 'https://news.ycombinator.com/news'


response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
texts = soup.get_text()

if '\n\n\n\n\n' in texts:
    texts = texts.split('\n\n\n\n\n')[1]

for i in range(29):
    print(texts.split('\n\n\n\n')[i].split('\n')[0])

