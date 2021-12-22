#Generates the hash table of each question ID and its complexity, and which class 
#it belongs to(easy,average,hard) based on percentile scores.

from scipy import stats
import os
curr_dir = os.getcwd() #For the relative structure.
f = open(curr_dir[:-20]+"/Data/CSV files/questions.csv",'r') #File containing all questions

#tagsDict and tagsDictPlain is a dictionary which maps
#the tags with the number of accepted submissions which
#is used to calculate the complexity of question.
tagsDict = dict()
tagsDictPlain = dict()
for i in f.readlines()[1:]:
	row = i.strip().split(",")
	titleTags = row[2].split("|")	#Pipe being the separator for a bunch of title tags
	for tag in titleTags:
		if tag not in tagsDict:
			tagsDict[tag] = [int(row[4])] #row[4] is the number of accepted submissions for that problem
		else:
			tagsDict[tag].append(int(row[4]))
	titleTags1 = row[3].split("|")	
	for tag in titleTags1:
		if tag not in tagsDictPlain:
			tagsDictPlain[tag] = [int(row[4])]
		else:
			tagsDictPlain[tag].append(int(row[4]))
			
#list of all the accepted submissions for each question the tag comes in.
a = []
for i in tagsDict:
	listOfTag = tagsDict[i]
	avg = stats.trim_mean(tagsDict[i],0.1) #Taking a trimmed mean so that outliers can be removed.
	tagsDict[i] = avg
	#avg = sum(tagsDict[i])/len(tagsDict[i])
	a.append([i,avg])
	#print(i,avg)
a.sort(key=lambda x:x[1])
m = a[len(a)-1][1]
for i in a:
	i[1] = (1 - i[1]/m)
tagsDict = dict(a)
del a 
#print(tagsDict)
allValues = []
#Increasing levels of complexity, 1 being the hardest and 0 being the easiest.
f.close()

f = open("questions.csv",'r')
g = open("questions-complexity.csv",'w')
string = f.readlines()
g.write(string[0].strip() + "," + "Complexity," + "Class" +"\n") #Each line in the new csv is the question id, complexity value, and its class.
for line in string[1:]:
	attrs = line.strip().split(",")
	line = line.strip()
	firstMax = max(list(map(lambda x: tagsDict[x],attrs[2].split("|"))))
	firstMax = float("{0:.3f}".format(firstMax))
	allValues.append(firstMax)
first = stats.scoreatpercentile(allValues,33) #The 33rd percentile indicates a threshold for the easy and average type problems
second = stats.scoreatpercentile(allValues,66) #The 66th percentile indicates a threshold for the medium and hard type problems
countE = 0
countH = 0
countM = 0
for i in range(0,len(string)-1):
	firstMax = allValues[i]
	complexity = float("{0:.3f}".format(firstMax))
	line = string[i+1].strip()
	if(complexity < first):
		classi = "Easy"
		countE+=1
	elif(complexity < second):
		classi = "Medium"
		countM+=1
	else:
		classi = "Hard"
		countH+=1
	g.write(line + "," + str(complexity)+"," + classi + "," +"\n")
	
f.close()
g.close()	
