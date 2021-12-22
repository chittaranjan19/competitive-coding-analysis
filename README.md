This repository involves exploratory analysis of competitive coding data.

Pre-requisites to use this project:
- python2
	- sklearn
	- scipy
	- lizard
- python3
	- bs4
	- urllib	

The directory structure: 

+ Data
	
	+ Section-1
		+ username
			- submissionID.txt : Contains the code the user wrote for that submission.
			- username.csv : Uncleaned csv file consisting of all the data scraped about the user's submissions.
			- username_m.csv : Cleaned csv file containing submissions only written in c++ language.
			- username_cleaned.csv : csv file containing all submissions in all languages but cleaned after fixing some minor errors.
			
	
	+ Section-2
		+ username
			- submissionID.txt : Contains the code the user wrote for that submission.
			- username.csv : Uncleaned csv file consisting of all the data scraped about the user's submissions.
			- username_m.csv : Cleaned csv file containing submissions only written in c++ language.
			- username_cleaned.csv : csv file containing all submissions in all languages but cleaned after fixing some minor errors.
			
			
	+ Section-3
		+ username
			- submissionID.txt : Contains the code the user wrote for that submission.
			- username.csv : Uncleaned csv file consisting of all the data scraped about the user's submissions.
			- username_m.csv : Cleaned csv file containing submissions only written in c++ language.
			- username_cleaned.csv : csv file containing all submissions in all languages but cleaned after fixing some minor errors.
			
			
	+ Section-4
		+ username
			- submissionID.txt : Contains the code the user wrote for that submission.
			- username.csv : Uncleaned csv file consisting of all the data scraped about the user's submissions.
			- username_m.csv : Cleaned csv file containing submissions only written in c++ language.
			- username_cleaned.csv : csv file containing all submissions in all languages but cleaned after fixing some minor errors.
			
			
	+CSV files
		- features_time.csv : csv file containing all the timed attributes for all the users.
		- features_non_time.csv : csv file containing all the skilled attributes for all the users.
		- questions-complexity.csv : csv file containing all the questions, with their tags, their accepted submissions, and their complexity.
		- questions.csv : csv file containing all the scraped questions and their tags and number of accepted submissions.
		

+Scripts
	+ Computation
		- questions.py : Generates the hash table of each question ID and its complexity, and which class. Writes this in questions-complexity.csv
	
	+ Features
		- features.py : Generates all the time dependent and the skilled(non-time) dependent attributes from the original set of attributes
	
	+ K-Means
		- kmeans.py : Clusters users based on the time dependent attributes. Generates a cluster plot of users.
		- kmeans_pca.py : First generates three components from the many skilled attributes using PCA, and runs k-means on these attributes.
		
	+ Scraping
		- questionScrape.py : Script to scrape all the questions, its tags, and number of accepted submissions from the codeforces website
		- section-1.py : Script to scrape random 50 users from rank 1-6000
		- section-2.py : Script to scrape random 50 users from rank 6000-12000
		- section-3.py : Script to scrape random 50 users from rank 12000-18000
		- section-4.py : Script to scrape random 50 users from rank 18000-24000
		
	+ Visualisations
		- pieChart.py : Generates a pie-chart for each section on how many easy/medium/hard problems they solve.
		- timerAll.py : Generates a plot of users against time they submit, to see which is the most common time coders are active.
		

