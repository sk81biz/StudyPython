import requests
from bs4 import BeautifulSoup
 
 
url = 'https://hub.docker.com/repository/docker/onlyoffice/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
 
urls = []
for link in soup.find_all('a'):
    print(link.get('href'))