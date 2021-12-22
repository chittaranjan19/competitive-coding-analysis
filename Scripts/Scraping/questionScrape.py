import time as tsleep
from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
import random as rd
droppedLinks = []
qpages = []
for i in range(1,33):	#Get all pages which contain problems
	qpages.append("http://codeforces.com/problemset/page/" + str(i))

f = open("questions.csv",'w') #Write to this file
#Headings of the csv file.
f.write("Problem ID"+","+"Problem Name"+","+"Title Tags"+","+"Plain Tags,"+"Number Solved"+"\n")
for qpage in qpages:
	try : 
		page = urlopen(qpage)
		tsleep.sleep(3)
	except Exception:
		qpages.append(qpage)
		continue
	soup = BeautifulSoup(page)
	table = soup.find_all('table',attrs={"class":"problems"})[0]
	rows = table.find_all('tr')[1:]
	print(qpage)
	for row in rows:
		cols = row.find_all('td')
		pid = cols[0].get_text().strip()
		pname,tags = cols[1].find_all('div')
		
		pname = "".join(pname.get_text().strip().split(","))
		tags = tags.find_all('a')
		num = cols[3].get_text().strip()[1:]
		keytags = []
		plaintags = []
		for i in tags:
			plaintags.append("".join(i.get_text().strip().split(",")))
			thetag = "".join(i['title'].split(","))
			keytags.append(thetag)
			#print(i['title'])
		kt = "|".join(keytags)	#Adding the key tags with separator |
		pt = "|".join(plaintags) #Adding the title plain tags with separator |
		
		f.write(pid+","+pname+","+kt+","+pt+","+num+"\n")
