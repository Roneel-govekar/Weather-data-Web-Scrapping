from requests_html import HTMLSession
import numpy as np
s=HTMLSession()


url1="http://www.citymayors.com/gratis/canadian_cities.html"
r1=s.get(url1,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"})
cities=[]
#print(r1.html.find("title",first=True).text[:-16])
#print(r1.html.find("table tr"))

tableRow=r1.html.find("table table tr td b")

for i in tableRow:
    cities.append(i.text)

cities.remove("Rank")
cities.remove("City")
cities.remove("Province")
cities.remove("Population")

ans=[]
fields=["Name","Temperature","Wind","Type"]
ans.append(fields)
for i in cities:
    url= f'https://www.google.com/search?q={i}+weather'
    row=[]
    r=s.get(url,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"})

    name=r.html.find("title",first=True).text[:-16]

    temp=r.html.find("span#wob_tm",first=True).text
    wind = r.html.find("span#wob_ws",first=True).text
    type = r.html.find("span#wob_dc",first=True).text 
    unit=r.html.find("div.vk_bk.wob-unit span.wob_t",first=True).text
    #row.extend([name,temp+unit,wind,type])
    row.append(name)
    row.append(temp+unit)
    row.append(wind)
    row.append(type)
    #print(row)
    ans.append(row)
#print(ans)

np.savetxt("weatherData.csv",ans,
delimiter=",",fmt="% s")
