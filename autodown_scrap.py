import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from selenium import webdriver

#drive = "C:\\tools\\geckodriver\\geckodriver.exe"
#C:\Python37\Drivers\geckodriver.exe
browser = webdriver.Chrome()
#browser = webdriver.Edge()

url = input("Link: ")
browser.get(url)
soup = BeautifulSoup(browser.page_source, "html.parser")

song = soup.find_all("p", attrs={"class":"hidden"})

print("Download one file peer 1 minute (60s)... Please, wait...")
for i in range(len(song)):
    url = song[i].attrs['data-href']

    if url == "music/1.wav" or url == "" or url == None:
        continue
        
    print(song[i].attrs['data-href'])
    browser.get(url)
    time.sleep(60)
print("Complete... See ya!")

browser.close()
