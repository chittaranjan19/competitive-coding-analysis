import glob
import matplotlib.pyplot as plt
import sys

#Relative directories. Replace with wherever the section folders are being stored.
#The absolute path, should change accordingly.
folders = glob.glob("/home/chittaranjan/Documents/3rd Year/5_DA/Project/TimeSeries/Section-1/*") + glob.glob("/home/chittaranjan/Documents/3rd Year/5_DA/Project/TimeSeries/Section-2/*") + glob.glob("/home/chittaranjan/Documents/3rd Year/5_DA/Project/TimeSeries/Section-3/*") + glob.glob("/home/chittaranjan/Documents/3rd Year/5_DA/Project/TimeSeries/Section-4/*")		#All users in the dataset


listOfTimes = []
for user in folders:
	
	userdeets = glob.glob(user+"/*.csv")
	
	f = open(userdeets[0])
	for line in f.readlines()[1:]:
		timestamp = line.strip().split(",")[1]
		hour = timestamp.split()[1].split(":")[0]	#Get the hour from the csv file for the user
		listOfTimes.append(int(hour))
Y = []
for i in range(1,25):
	Y.append(listOfTimes.count(i))


#____PLOTTING____#

fig = plt.figure()
ax = fig.add_subplot(111)

	
ax.plot(range(1,25),Y)
ax.set_xlabel('Time (hours)')
ax.set_ylabel('No. of Submissions')

plt.show()
