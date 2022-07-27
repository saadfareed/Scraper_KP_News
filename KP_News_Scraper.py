from bs4 import BeautifulSoup   # Import BeautifulSoup
import requests #library to get the html code
import pandas as pd #library to create dataframes
url="https://pndkp.gov.pk/blog-grid/"   #url of the website to be scraped
html_text=requests.get(url).text    #get the html code of the website
soup=BeautifulSoup(html_text,"html.parser") #create a soup object             
# soup=soup.find_all("ul",{"class":"wgl-pagination"})
soup=soup.select("li.page") #select the tag with class "page"
page=1 #initialize the page number
mydict={"ID":[],"Worktype":[],"Type":[],"filepath":[],"location":[]} #create a dictionary to store the data
for i in soup:  #iterate through the list of tags
    i=i.text    #get the text of the tag
    if(i.isdigit() and int(i)>page):    #if the text is a number and it is greater than the current page
        page=int(i) #update the page number
#print(page)

f=open ("NKU.csv","w")  #open a file to write the data
f.write("ID,WorkType,Type,Filepath,location\n") #write the header
id=40000 #initialize the id
for i in range(1,page+1):   #iterate through the pages
    print((i/(page+1)*100),"%") #print the progress
    url="https://pndkp.gov.pk/blog-grid/"+"page/"+str(i)+"/"    #update the url
    html_text=requests.get(url).text    #get the html code of the website
    soup=BeautifulSoup(html_text,"html.parser") #create a soup object
    elms = soup.select("div.blog-post_media_part img")  #select the tag with class "blog-post_media_part"
    elms1 = soup.select("h3.blog-post_title")   #select the tag with class "blog-post_title"
    for i in elms1: #iterate through the list of tags
        mydict["Worktype"].append(i.text) #append the text of the tag to the dictionary
        mydict["location"].append("Khyber Pakhtunkhwa") #append the location to the dictionary
    for i in elms:      #iterate through the list of tags
        mydict["filepath"].append(i.attrs["src"])   #append the filepath to the dictionary
        mydict["Type"].append("Planning and Development")   #append the type to the dictionary
        mydict["ID"].append(id) #append the id to the dictionary
        id=id+1 #update the id
        
for data in zip(mydict["ID"],mydict["Worktype"],mydict["Type"],mydict["filepath"],mydict["location"]):  #iterate through the dictionary
    data=list(data) #convert the tuple to a list
    for i in data:  #iterate through the list
        datains=str(i)  #convert the element to a string
        datains=datains.replace(",", "")    #remove the commas
        f.write(datains)    #write the data to the file
        f.write(",")    #write the comma to the file
    f.write("\n")   #write the new line to the file
f.close()   #close the file
exit()  #exit the program


