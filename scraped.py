import requests
from bs4 import BeautifulSoup
url = 'https://github.com/trending'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
repos = soup.find_all('a', class_='Link')
for repo in repos:
    print(repo.contents)
