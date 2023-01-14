from bs4 import BeautifulSoup
import requests

url = "https://www.geeksforgeeks.org/python-programming-language/"
response = requests.get(url)
data = response.text
soup = BeautifulSoup(data, 'html.parser')
tags = soup.find_all('a')
for tag in tags:
    print(tag.get('href'))

titles = soup.find_all('a',{"class":"result-title"})



