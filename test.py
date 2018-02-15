import requests
from bs4 import BeautifulSoup

page = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
print('Status code: ' + str(page.status_code))
# print(page.content)
soup = BeautifulSoup(page.content,'html.parser')

# print(soup.prettify())
# html = list(soup.children)[2]
# body = list(html.children)[3]
# p = list(body.children)[1]
# print(p.get_text())

p = soup.find_all('p',id = 'second',class_ = 'outer-text');
print(p)

p = soup.select('div p')
print(p)
