from bs4 import BeautifulSoup
import requests
import pandas as pd
with open('free_proxy.txt','r') as f:
    proxies=f.read().split('\n')
header={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        'referer':"https://www.zameen.com/Homes/Islamabad-3-1.html"}
urls=[]
dict={'Karachi':'2','Islamabad':'3','Lahore':'1','Abbottabad':'385','Rawalpindi':'41','Multan':'15'
    ,'Abdul_Hakim':'10594','Ahmedpur_East':'12360','Bahawalpur':'23',"Faisalabad":'16'}
for i,city in enumerate(dict):
    print(i+1,"City : ",city)
city_name=input('Enter the name of city : ')   
for i in range(1,11):
    urls.append(str('https://www.zameen.com/Homes/'+city_name+'-'+(dict[city_name])+'-'+str(i)+'.html'))
    print(urls[i-1])
data={'Title':[],'location':[],'Price':[],'urls':[]}    
for i in urls:    
    page=requests.get(i,proxies={'http':proxies[3]})
    soup = BeautifulSoup(page.text, "html.parser")
    spans=soup.find_all(class_="f343d9ce")
    counter=0
    for span in spans:
        data['Price'].append(span.get_text())
    spans=soup.find_all(class_="c0df3811")
    for span in spans:
        data["Title"].append(span.get_text())
    spans=soup.find_all(class_="_162e6469")
    for span in spans:
        data["location"].append(span.get_text())    
    spans=soup.find_all(class_="_7ac32433")    
    for span in spans:
        if span.get("href")==None:
            continue
        else:
            data["urls"].append('https://www.zameen.com/'+str(span.get("href")))
df=pd.DataFrame.from_dict(data)
df.to_csv("data.csv",index=False)     
