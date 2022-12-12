import requests
from bs4 import BeautifulSoup


url = 'https://ful.io'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')

urls = []
for link in soup.find_all('a'):
    urls.append(link.get('href'))


print("social links")
# print(urls)
print(urls[17])
print(urls[18])

print(".......................")

print("Email/s-")
print(urls[30])

print(urls[31])