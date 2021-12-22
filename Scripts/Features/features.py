from __future__ import division
import glob as gl
import csv
import lizard
import itertools


f = open("features_time.csv",'w') #CSV file containing all the time dependent attributes
g = open("features_non_time.csv",'w') #CSV file containing all the skill dependent attributes
f.write("Username,# of Submissions,# of Problems,# of problems accepted\n")
g.write("Username,Avg Compilation Errors,Avg Logic Errors,Code Complexity,Accuracy accepted,Languages used,Questions complexity\n")
regex = "Section-*" #The glob module can check for folders satisfying this regex.

QInfo = [] 
#Schema is problem id,problem name,title tags,plain tags,number of questions solved,complexity, class, normalized solved
with open('questions-complexity.csv', 'rb') as k:
	reader = csv.reader(k)
	for row in reader:
		QInfo.append(row)

QComplex = {} #dictionary of question ids with their complexities so it can be used for lookup
for row in QInfo:
	QComplex[row[0]] = row[5]

#Assuming all the section folders are on the same directory as this script
sections = gl.glob(regex)
for onesection in sections:
	users = gl.glob(onesection+"/*") #Go to that section
	for oneuser in users:
		complexities = []
		try:
			csvname = gl.glob(oneuser+"/"+oneuser[7:]+"_cleaned.csv")[0] #Cleaned file containing all the cleaned data for a user.
		except Exception:
			print "Empty folder or trying to open a file not existing"
			continue
		csvfile = open(csvname,'r')
		csvobject = list(csv.reader(csvfile,delimiter=","))
		numOfSubs = len(csvobject) - 1			#Counts attribute headings also, hence the -1
		probs = set(map(lambda x: x[2],csvobject))
		probs.discard("Problem")
		numOfProbs = len(probs)
		totcerrors = 0
		totlerrors = 0
		wtavg = 0
		accepted = 0
		submissions = 0
		languages = set()
		probs_complexity = []
		for oneproblem in probs:
			submissionsforproblem = [i for i in csvobject if oneproblem in i]
			probID = oneproblem.split("-")[0].strip()
			if probID in QComplex:
				probs_complexity.append(QComplex[probID]) #List of all complexities for the problems the user has solved.
			else:
				#print(oneuser+ ", No such problem : "+probID)
				pass
			persubmissionsloc = []
			for asubmission in submissionsforproblem:
				if "Compilation error" in asubmission:
					totcerrors += 1
				if asubmission[4].startswith("Wrong answer"):
					totlerrors += 1
				if "Accepted" in asubmission[4]:
					accepted+=1
				languages.add(asubmission[3])
				codefile = open(oneuser+"/"+str(asubmission[0])+".txt") #Open his code file
				loc = len(codefile.read().split("\n"))
				ldic = lizard.analyze_file(oneuser+"/"+str(asubmission[0])+".txt")
				m = 0
				for func in ldic.function_list: #Compute the average code complexity for a user using cyclomatic complexity.
					if func.cyclomatic_complexity > m:
						m = func.cyclomatic_complexity
				complexities.append(m)
				persubmissionsloc.append(loc)
				codefile.close()
				submissions+=1
			linesadded = persubmissionsloc[len(persubmissionsloc) - 1] - persubmissionsloc[0]
			wtavg += linesadded/persubmissionsloc[len(persubmissionsloc) - 1]
		try:
			#in case some guy does not use c++ at all.
			#Computing all averages.
			avgcerrors = "{0:.3f}".format(float(totcerrors/numOfProbs))
			avglerrors = "{0:.3f}".format(totlerrors/numOfProbs)
			avgwtavg = "{0:.3f}".format(wtavg/numOfProbs)
			avgAccept = "{0:.3f}".format(accepted/submissions)
			avgcompl = sum(complexities)/len(complexities)
			languagesUsed = len(languages)
			qcompl = sum(list(map(float,(probs_complexity))))/len(probs_complexity)
		except:
			continue
			
		name = oneuser.split("/")[1]
		#("Username,# of Submissions,# of Problems,Avg Compilation Errors,Avg Logic Errors,Avg Delta LOC")
		f.write(name+","+str(numOfSubs)+","+str(numOfProbs)+","+str(accepted)+"\n")
		g.write(name+","+str(avgcerrors)+","+str(avglerrors)+","+str(avgcompl)+","+str(avgAccept)+","+str(languagesUsed)+","+str(qcompl)+"\n")
		
		print("Done with "+oneuser)

