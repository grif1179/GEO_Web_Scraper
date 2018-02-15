import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.ncbi.nlm.nih.gov/gds/?term=Ribo+zero");
print('Status code: ' + str(page.status_code))

soup = BeautifulSoup(page.content,'html.parser')

containers = soup.find_all("div",{"class":"rprt"})

filename = "riboLinks.csv"
file = open(filename,"w")

headers = "link, linkText\n"
file.write(headers)

for container in containers:
    linkContainer = container.p.a
    link = "https://www.ncbi.nlm.nih.gov" + linkContainer['href']
    linkText = linkContainer.text.strip()
    # print(linkContainer)
    print(link)
    print(linkText)
    print('\n')
    file.write(link + ',' + linkText.replace(",","|") + "\n")

file.close()
