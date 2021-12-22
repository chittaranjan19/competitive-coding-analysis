import time as tsleep
from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
import random as rd
droppedLinks = []
leaderboard = []
for i in range(90,116):	#Get all links of the leaderboard pages for section-4.
	leaderboard.append("http://codeforces.com/ratings/page/" + str(i))


#print("Leaderboards link generation done")	#Markers to know what part of the loop has finished.

for oneRankList in leaderboard:	#For each page of the 25 pages

	try:
		print("Getting",oneRankList)
		pageOfUsers = urlopen(oneRankList)
	except Exception:
		print("Something went wrong. Waiting and re-trying.")
		tsleep.sleep(7)
		try:
			pageOfUsers = urlopen(oneRankList)
		except Exception:
			droppedLinks.append(oneRankList)
			continue
			
	print("Got",oneRankList)		
	soupOfUsers = BeautifulSoup(pageOfUsers)
	table = soupOfUsers.find_all('div',attrs={"class":"datatable ratingsDatatable"})[0].find_all("table")
	users = table[0].find_all('a',attrs={"class":"rated-user"})
	allranks = list(map(lambda x : x.find('td').get_text().strip(),table[0].find_all('tr')[1:]))
	r1 = rd.randint(0,len(users)-1)
	r2 = rd.randint(0,len(users)-2)
	if r1 == r2:
		r2 += 1
	firstRandomUser = users[r1]
	secondRandomUser = users[r2]
	#print("Random users picked")
	num = leaderboard.index(oneRankList)
	for user in (firstRandomUser,secondRandomUser):

		username = user.get_text().strip()
		#userRank = users.index(user) + 1 + (200*num) 
		userRank = allranks[users.index(user)]
		submissionLink = "http://codeforces.com/submissions/" + username

		if os.path.isdir(username):
			os.system("rm -r "+username)
		os.mkdir("/home/chittaranjan/Documents/3rd Year/5_DA/Project/Section-4/"+username) #CHANGE THIS AS PER YOUR DIRECTORY STRUCTURE
		f = open(username+"/"+username+".csv",'w')
		f.write("ID,Timestamp,Problem,Lang,Verdict,Time,Memory,Rank:"+str(userRank)+"\n")
		

		
		
		
		try:
			print("Getting",submissionLink)
			pageOfSubs = urlopen(submissionLink)
		except Exception:
			print("Something went wrong. Waiting and re-trying.")
			tsleep.sleep(7)
			try:
				pageOfSubs = urlopen(submissionLink)
			except Exception:
				droppedLinks.append(submissionLink)
				continue		
		print("Got",submissionLink)
		soupOfSubs = BeautifulSoup(pageOfSubs)
		
		#print("Processed first submissions page")
	
		pagination = soupOfSubs.find_all('div',attrs={"class":"pagination"})
		if len(pagination) > 1:
			print("PAG:",pagination)
			pagination = pagination[1]
			n = int(pagination.find_all('li')[-2].get_text())	#Get the number of submission pages there are.

			submissionLinks = []		
			for i in range(1,n+1):	#Gather every submissions page
				submissionLinks.append("http://codeforces.com/submissions/"+username+"/page/"+str(i))
		else:
			submissionLinks = [submissionLink]
		#print("Submissions pages link generation done")
		
		for submissionLink in submissionLinks:	#Run through every link, and extract data that is needed
			
			try:
				if len(submissionLinks) > 1:
					print("Getting",submissionLink)
					pageOfSubs = urlopen(submissionLink)
				
			except Exception:
				print("Failed; Waiting 5 seconds and re-trying")
				print("Waiting...")
				tsleep.sleep(5)
				try:
					pageOfSubs = urlopen(submissionLink)
				except Exception:
					droppedLinks.append(submissionLink)
					continue

			print("Got",submissionLink)
			if len(submissionLinks) > 1:
				soupOfSubs = BeautifulSoup(pageOfSubs)
			submissionTableSoup = soupOfSubs.find_all('table',attrs={"class":"status-frame-datatable"})[0]
			
			
			if(not submissionTableSoup):
				continue
			submissionTable = []
			allRecords = submissionTableSoup.find_all('tr')[1:]
		
			for aRecord in allRecords:	#Gets the table entries like id,timestamp etc
				tds = aRecord.find_all('td')
				subId = tds[0].get_text().strip().strip(",")
				timeStamp = tds[1].get_text().strip().strip(",")
				problem = tds[3].get_text().strip().strip(",")
				lang = tds[4].get_text().strip().strip(",")
				verdict = tds[5].get_text().strip().strip(",")
				time = tds[6].get_text().strip().strip(",")
				memory = tds[7].get_text().strip().strip(",")
			
				
				contestNum = problem.split("-")[0].strip()[:-1]
				codeLink = "http://codeforces.com/contest/"+contestNum+"/submission/"+subId
				try:
					print("Getting",codeLink)
					pageOfCode = urlopen(codeLink)
				except Exception:
					print("Something went wrong. Waiting and re-trying")
					tsleep.sleep(7)
					try:
						pageOfCode = urlopen(codeLink)
					except Exception:
						droppedLinks.append(codeLink)
						continue
				print("Got",codeLink)	
				soupOfCode = BeautifulSoup(pageOfCode)
				
				#print("Retrieved code page")
				try:
					code = soupOfCode.find_all('pre',attrs={"class":"prettyprint program-source"})[0]
				except Exception:
					continue
				g = open(username+"/"+subId+".txt",'w')
				theCode = code.get_text()
				g.write(theCode)
				g.close()
				#LOC = len(theCode.split("\n"))
				submissionTable.append((subId,timeStamp,problem,lang,verdict,time,memory))
				print(subId,timeStamp,problem,lang,verdict,time,memory)

			for r in submissionTable:
				f.write(",".join(r)+"\n")	#Write onto the file (this happens for every submissions page)
				#print(",".join(r),"\n")
		
		#SubID 	TimeStamp  	Problem  Lang 	Verdict Time 	Memory
		
		f.close()	
	
if droppedLinks:
	dl = open(username+"/DROPPEDLINKS.txt",'w')
	for i in droppedLinks:
		dl.write(str(i)+"\n")	
