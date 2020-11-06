from urllib.request import *
from bs4 import BeautifulSoup

html = urlopen("https://stepik.org/media/attachments/lesson/209723/3.html").read()
soup = BeautifulSoup (html, 'html.parser')
sum = 0

for tag in soup.find_all('td'):
    sum += int(tag.get_text())
print(sum)

