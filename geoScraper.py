import requests
from bs4 import BeautifulSoup
# from selenium import webdriver
import helperFns

filename = 'riboLinks.csv'
helperFns.saveAsCSV(filename)
links = helperFns.getBaseAddr()
for link in links:
    articleText = link[0].replace(",","|") + ","
    organismName = helperFns.getOrganism(link[1]) + ","
    sampleLinks = helperFns.getSampleLinks(link[1])
    print(sampleLinks)
    for i in range(0,len(sampleLinks)):
        sraLink = helperFns.getSRALink(sampleLinks[i])
        if(sraLink == None):
            continue
        else:
            fastDumpCmd = helperFns.getFastDumpLink(sraLink)
            row = articleText + organismName.replace(",","|")+ "," + fastDumpCmd + '\n'
            helperFns.appendCSV(filename,row)
