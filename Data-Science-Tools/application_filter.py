''' 
Decision Tree  V.1
	Simple tool for a company to screen applications in the hiring process

Coded By: Tyler Linne
Date: 4/27/16
'''
#Import required packages 
import numpy as np
import pandas as pd
import pydot 
from sklearn import tree
from IPython.display import Image  
from sklearn.externals.six import StringIO  
from sklearn.ensemble import RandomForestClassifier

#Import a csv file holding the data the tree needs
input_file = "c:/UserName/user/documents/hire_data.csv"
df = pd.read_csv(input_file, header = 0)

#Set text values in csv to numerical values  
d = {'Y': 1, 'N': 0}
df['Hired'] = df['Hired'].map(d)
df['Currently Employed?'] = df['Currently Employed?'].map(d)
df['Private School'] = df['Private School'].map(d)
df['State School'] = df['State School'].map(d)
df['Top-tier school'] = df['Top-tier school'].map(d)
df['Internship'] = df['Internship'].map(d)

d = { 'AS': 0 'BS': 1, 'MS': 2, 'PhD': 3}
df['Level of Education'] = df['Level of Education'].map(d)
df.head()

#Filter out headers that hold various canidate data 
features = list(df.columns[:7])

#Create the tree using the desired header and the seperated headers list 
y = df["Hired"]
X = df[features]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,y)


#Displaying the tree in a readable format 
dot_data = StringIO()  
tree.export_graphviz(clf, out_file=dot_data,  
                         feature_names=features)  
graph = pydot.graph_from_dot_data(dot_data.getvalue())  
Image(graph.create_png())  


#Test the validity of the tree using the "Random Forest" methood with a factor of 25 seperate tests 
clf = RandomForestClassifier(n_estimators=25)
clf = clf.fit(X, y)

#Predict employment of an employed 10-year veteran with an AS Degree
print clf.predict([[10, 1, 4, 0, 0, 0, 0]])
#...and an unemployed 10-year veteran with an AS Degree
print clf.predict([[10, 0, 4, 0, 0, 0, 0]])
