from bs4 import BeautifulSoup
from bs4 import SoupStrainer
from json import JSONEncoder
import json
gpaid = "#"+"LblGPA"
nameid = "#"+"LblName"
rollid = "#"+"LblEnrollmentNo"

soup = BeautifulSoup(open("civil_sr.html"))
#print(soup.prettify())

gpasoup = soup.select(gpaid)
namesoup = soup.select(nameid)
rollsoup = soup.select(rollid)

subs = soup.find_all("table", class_="DataGrid")

def returnsubs(sub):
    substr = ""
    sublist = sub.find_all("tr", class_="DataGridItem") + sub.find_all("tr", class_="DataGridAlternatingItem")
    for elem in sublist:
        subname = elem.find_all("font")[2].contents[0]
        subgrade = elem.find_all("font")[4].contents[0]
        substr = substr + subname + ":" + subgrade + "<br>"
    return substr     
    

subsoup =[]
for table in subs:
    subsoup.append(returnsubs(table))
    
#print(subsoup)



def retval(stud):
    return stud.find_all("font")[0].contents[0]
 
gpalist = []

for i in range(len(gpasoup)):
    d = {}
    d['name'] = retval(namesoup[i])
    d['gpa'] = retval(gpasoup[i])
    d['roll'] = retval(rollsoup[i])
    d['mark'] = subsoup[i]
    
    gpalist.append(d)
    #print retval(gpasoup[i]), retval(namesoup[i]), retval(rollsoup[i])


for i in range(len(gpalist)):
    for j in range(i,len(gpalist)):
        if(gpalist[i]["roll"]>gpalist[j]["roll"]):
            gpalist[i],gpalist[j] = gpalist[j],gpalist[i]
                
#print(gpalist)

sub_json = JSONEncoder().encode(gpalist)

#print(sub_json)

with open('data3.json', 'w') as outfile:
  json.dump(sub_json, outfile)