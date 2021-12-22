import glob
import csv
#Assuming this file is on the same folder as this script
f = open("questions-complexity.csv")		#File to lookup question complexity previously calculated
text = f.readlines()[1:]
hashMap = dict()
for i in text:
	new_list = i.split(",")
	hashMap[new_list[0]] = new_list[-2]	#Create a dict to store question id and its complexity.

allFolders = glob.glob("*")
python = glob.glob("*.py")
allFolders.remove(python[0])
#print allFolders
all_probs = set()
for folder in allFolders:		#Iterate through every user
	try:
		csvname = glob.glob(folder+"/"+"*.csv")[0]
	except Exception:
		continue
	csvfile = open(csvname,'r')
	csvobject = list(csv.reader(csvfile,delimiter=","))
	numOfSubs = len(csvobject) - 1			#Counts attribute headings also, hence the -1
	probs = list(set(map(lambda x: x[2].split("-")[0].strip(),csvobject)))
	all_probs = all_probs.union(set(probs))		#Get the unique problems the user has attempted

	probs.remove("Problem")

splitup = {"Easy":0,"Medium":0,"Hard":0}
for pb in all_probs:		#count the number of times a problem of each category has been solved.
	try:
		splitup[hashMap[pb]] += 1
	except Exception:
		continue

import matplotlib.pyplot as plt

#___________________PIE CHART PLOTTING_____________________#

labels = splitup["Easy"],splitup["Medium"], splitup["Hard"]
sizes = [splitup["Easy"],splitup["Medium"], splitup["Hard"]]
colors = ['green', 'orange', 'red']
explode = (0, 0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

plt.pie(sizes,explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)
# Set aspect ratio to be equal so that pie is drawn as a circle.
plt.axis('equal')
plt.title('Ranks 1 to 6000')
#fig = plt.figure()
plt.show()
