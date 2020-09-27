import requests
from bs4 import BeautifulSoup

response = requests.get('https://en.wikipedia.org/wiki/Ruth_Bader_Ginsburg')

soup = BeautifulSoup(response.content, 'html.parser')

links = soup.find_all('a', href=True)

baseURL = 'https://en.wikipedia.org'

print(baseURL + links[0]['href'])

response = requests.get(baseURL + links[0]['href'])

print(response)

'''

email me abemery@clemson.edu if you have any questions!

Happy Hacking,

Drew

'''
