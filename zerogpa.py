from __future__ import division
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
        subcred = elem.find_all("font")[3].contents[0]
        substr = substr + subname + ":" + subcred + ":" + subgrade + "<br>"
    return substr

def returngpa(sub):
    l = sub.split("<br>")
    k =[]
    g = {'S':10,'A':9,'B':8,'C':7,'D':6,'E':5,'F':0}
    tcred = 0
    tval = 0
    for a in l:
        k.append(a.split(":"))

    for i in range(len(k)-1):
        a = k[i]
        tval = tval+g[a[2]]*int(a[1])
        tcred = tcred + int(a[1])
        #print(a[1],a[2])
    #print(tval,tcred)
    return "%.2f" % (tval/tcred)


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
    d['zero'] = "false"

    if(retval(gpasoup[i])=="0"):
        d['zero'] = "true"
        d['gpa'] = returngpa(subsoup[i])
        #print("\n")

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
