import requests
import re
from bs4 import BeautifulSoup
# from selenium import webdriver

def getBaseAddr():
    page = requests.get("https://www.ncbi.nlm.nih.gov/gds/?term=Ribo+zero");
    print('Status code: ' + str(page.status_code))
    soup = BeautifulSoup(page.content,'html.parser')
    containers = soup.find_all("div",{"class":"rprt"})
    links = []
    for container in containers:
        linkContainer = container.p.a
        link = "https://www.ncbi.nlm.nih.gov" + linkContainer['href']
        linkText = linkContainer.text.strip()
        links.append([linkText,link])
    return links;

def getOrganism(link):
    page = requests.get(link)
    soup = BeautifulSoup(page.content,'html.parser')
    container = soup(text=re.compile('^Organism$'))
    if(len(container) == 0):
        container = soup(text=re.compile('^Organisms$'))
    organism = container[0].parent.find_next_sibling('td').a
    organismName = organism.text
    while(organism.find_next_sibling('a') != None):
        organism = organism.find_next_sibling('a')
        organismName += " | " + organism.text
    return organismName

def getSampleLinks(link):
    page = requests.get(link)
    soup = BeautifulSoup(page.content,'html.parser')
    containers = soup.find_all("a",{"onmouseover":"onLinkOver('HelpMessage' , geoaxema_recenter)"})
    sampleLinks = []
    for container in containers:
        sampleLinks.append("https://www.ncbi.nlm.nih.gov" + container['href'])
    regex = re.compile(r'.GSM')
    sampleLinks = list(filter(regex.search,sampleLinks))
    print(sampleLinks)
    return sampleLinks;

def getSRALink(sampleLink):
    page = requests.get(sampleLink)
    print('Status code: ' + str(page.status_code))
    soup = BeautifulSoup(page.content,'html.parser')
    containers = soup(text=re.compile('^SRA$'))
    if(len(containers) == 0):
        return None;
    else:
        for container in containers:
            if(container.parent.find_next_sibling('td') != None):
                return container.parent.find_next_sibling('td').find('a')['href'];

def getFastDumpLink(sraLink):
    page = requests.get(sraLink)
    print('Status code: ' + str(page.status_code))
    soup = BeautifulSoup(page.content,'html.parser')
    table = soup.find('table')
    fastDumpLink = table.find("td",{"align":"left"}).a.text
    fastDumpCmd = generateFastDumpCmd(fastDumpLink)
    return fastDumpCmd;

def generateFastDumpCmd(sra):
    fastDumpCmd = "fastq-dump -I --split-files " + sra
    return fastDumpCmd;

def saveAsCSV(filename):
    file = open(filename,"w")
    headers = "Article Text, Organism, fastq cmd\n"
    file.write(headers)
    file.close()
    return;

def appendCSV(filename,row):
    file = open(filename,"a")
    file.write(row)
    file.close()
    return;
