#Cluster users based on the time dependent attributes.
from sklearn.cluster import KMeans
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import glob

#Assuming the file is on the same folder as this script.
f = open("features_time.csv") #Cluster based on the time dependent attributes, to check if they 
#align with the ranks given by the website.
f.readline() #To skip the header.
X = []
Y = []
accepted = []
for i in f:
	
	Y.append(i.split(",")[0]) #Append the user names to Y.
	row = list(map(float,i.strip().split(",")[1:]))
	accepted.append(row[2])
	X.append([row[-1],row[-2],row[-3]]) #The three attributes that are time dependent.
	
kmeans = KMeans(n_clusters=3).fit(X) 
#Train it unsupervised to make three clusters denoting the different sections.


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

result = open("result.csv",'w')
result.write("Username,Cluster,Section\n")



#ax.set_autoscalex_on(False)
#ax.set_xlim([-0.5,0.5])
xs = []
ys = []
zs = []
thecolor = []
for i in X:
    xs.append(i[0])
    ys.append(i[1])
    zs.append(i[2])
    cc = kmeans.labels_[X.index(i)]
    #Set the colours to the labels
    if cc == 0:
    	co = 'r'
    if cc == 1:
    	co = 'g'
    if cc == 2:
    	co = 'b'
    thecolor.append(co)

section0 = []
section1 = []
section2 = []
section3 = []

#section1 consists of section1
#section2 consists section2 as well as section3.
#section3 consists only of section4.

#Relative file structure required where the data is stored,i,e
#where all the section folders are present.
#should be changed to the absolute structure of the sections accordingly.
section1.extend(glob.glob("/home/vishal/Documents/5th sem/DA/Project/Section-1/*"))
section2.extend(glob.glob("/home/vishal/Documents/5th sem/DA/Project/Section-2/*"))
section2.extend(glob.glob("/home/vishal/Documents/5th sem/DA/Project/Section-3/*"))
section3.extend(glob.glob("/home/vishal/Documents/5th sem/DA/Project/Section-4/*"))


section1 = list(map(lambda x:x.split("/")[-1],section1))
section2 = list(map(lambda x:x.split("/")[-1],section2))
section3 = list(map(lambda x:x.split("/")[-1],section3))
for name,clus in zip(Y,kmeans.labels_):
	sec = -1
	if name in section1:
		sec = 2
	elif name in section2:
		sec = 0
	elif name in section3:
		sec = 1
	
	result.write(name+","+str(clus) +","+str(sec)+"\n")
	#result.csv can be used to evaluate the clusters, but not very accurately, as 
	#the resulting clusters may belong to any one of the sections.
ax.scatter(xs, ys, zs,c=thecolor)

'''
for c, m, zl, zh in [('r', 'o', -50, -25), ('b', '^', -30, -5)]:
    xs = randrange(n, 23, 32)
    ys = randrange(n, 0, 100)
    zs = randrange(n, zl, zh)
    ax.scatter(xs, ys, zs, c=c, marker=m)
'''
ax.set_xlabel('Accuracy')
ax.set_ylabel('Problems')
ax.set_zlabel('Complexity')

plt.show() #Show the plot

result.close()
