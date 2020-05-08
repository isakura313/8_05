from bs4 import BeautifulSoup

with open("index.html") as html_doc:
    content = html_doc.read()

soup = BeautifulSoup(content, 'html.parser')
# print(soup.prettify())
# print(soup)
print(type(soup))
print(soup.h1)
print(soup.h1.string)

print(type(soup.find_all('a')))
data= soup.find_all('p')
for i in data:
    print(i.string)