import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')
print(r.url)
print(r)
print(r.status_code)
soup = BeautifulSoup(r.content, 'html.parser')

print(soup.title)
print(soup.title.name)
print(soup.title.parent.name)

s = soup.find('div', id= 'main')
leftbar = s.find('ul', class_='leftBarList')
content = leftbar.find_all('li')
for cont in content:
    print(cont)

#s = soup.find('div', class_='entry-content')
#lines = s.find_all('p')

#for line in lines:
#    print(line.text)