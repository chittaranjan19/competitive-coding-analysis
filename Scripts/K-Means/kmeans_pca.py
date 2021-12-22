import numpy as np
from sklearn.decomposition import PCA
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D
import os

Users = []
Attributes = [] 
#Assuming file is on the same folder as the script.
f = open("features_non_time.csv") #The final csv file which contains every skilled attribute normalized
f.readline()
for i in f:
	Users.append(i.split(",")[0])
	row = list(map(float,i.strip().split(",")[1:]))
	
	Attributes.append(row)

			
pca = PCA(n_components=3) #Defining the number of required new attribues is 3.
pca.fit(Attributes) #Fit all the attributes given on three axes.

Attributes2 = pca.fit_transform(Attributes) #Transform it to three dimensions for k-means.

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

kmeans = KMeans(n_clusters=3).fit(Attributes2)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#The three axes set by the PCA, which have no semantics.
ax.set_xlabel('Component 1')
ax.set_ylabel('Component 2')
ax.set_zlabel('Component 3')

xs = []
ys = []
zs = []
thecolor = []
Attributes2 = list(map(list,Attributes2)) #new attributes
for i in Attributes2:
    xs.append(i[0])
    ys.append(i[1])
    zs.append(i[2])
    print list(i)
    print Attributes2[0]
    cc = kmeans.labels_[Attributes2.index(i)]
    if cc == 0:
    	co = 'r'
    if cc == 1:
    	co = 'g'
    if cc == 2:
    	co = 'b'
    thecolor.append(co)

#Assuming the section folders are on the same folder as the script.
section1 = os.listdir(os.getcwd()+"/Section-1")
section2 = os.listdir(os.getcwd()+"/Section-2")
section2 = os.listdir(os.getcwd()+"/Section-3")
section3 = os.listdir(os.getcwd()+"/Section-4")

#result.csv contains the clusters and the sections they come in.
result = open("Result.csv",'w')
result.write("Component 1,Component 2,Component 3\n")
	
for name,clus in zip(Users,kmeans.labels_):
	sec = -1
	if name in section1:
		sec = "section1"
	elif name in section2:
		sec = "section2"
	elif name in section3:
		sec = "section3" 
	
	result.write(name+","+str(clus)+"$" +","+str(sec)+"\n")
	
ax.scatter(xs, ys, zs,c=thecolor)



plt.show()

result.close()
