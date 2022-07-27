from tkinter import W
from selenium import webdriver  # for chrome open library for scraping
import os
import time #time library for sleep
from selenium.webdriver.common.keys import Keys  # chrome keys libraries for input forms
from selenium.webdriver.common.action_chains import ActionChains #performing action libraries in chrome like Enter ESC
from bs4 import BeautifulSoup, NavigableString #Libraries to parse HTML  
from bs4 import BeautifulSoup
import requests #library to get the html code
import pandas as pd
url="https://pndkp.gov.pk/blog-grid/"
html_text=requests.get(url).text
soup=BeautifulSoup(html_text,"html.parser")
# soup=soup.find_all("ul",{"class":"wgl-pagination"})
soup=soup.select("li.page")
page=1
mydict={"ID":[],"Worktype":[],"Type":[],"filepath":[],"location":[]}
for i in soup:
    i=i.text
    if(i.isdigit() and int(i)>page):
        page=int(i)
#print(page)

f=open ("NKU.csv","w")
f.write("ID,WorkType,Type,Filepath,location\n")
id=40000
for i in range(1,page+1):
    print((i/(page+1)*100),"%")
    url="https://pndkp.gov.pk/blog-grid/"+"page/"+str(i)+"/"
    html_text=requests.get(url).text
    soup=BeautifulSoup(html_text,"html.parser")
    elms = soup.select("div.blog-post_media_part img")
    elms1 = soup.select("h3.blog-post_title")
    for i in elms1:
        mydict["Worktype"].append(i.text)
        mydict["location"].append("Khyber Pakhtunkhwa")
    for i in elms:
        mydict["filepath"].append(i.attrs["src"])
        mydict["Type"].append("Planning and Development")
        mydict["ID"].append(id)
        id=id+1
        
for data in zip(mydict["ID"],mydict["Worktype"],mydict["Type"],mydict["filepath"],mydict["location"]):
    data=list(data)
    for i in data:
        datains=str(i)
        datains=datains.replace(",", "")
        f.write(datains)
        f.write(",")
    f.write("\n")
f.close()
#(mydict)
exit()


