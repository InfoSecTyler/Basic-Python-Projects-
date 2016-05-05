'''
Titanic Survival Factors 
	A data analysis project using Kaggle Titanic's data set to determine
	what factors helped or hurt chances of surviving the Titanic 

Coded By: Tyler Linne
Date: 5/1/16
'''

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pandas import Series,DataFrame
%matplotlib inline

# Set up the Titanic csv file as a DataFrame
titanic_df = pd.read_csv('train.csv')

# Seperate between two sexes and children 
def male_female_child(passenger):
	'''Takes all passengers and defines anyone < 16 as a child'''
    age,sex = passenger
    if age < 16:
        return 'child'
    else:
        return sex
    

# Add the result of the function to the dataframe 
titanic_df['person'] = titanic_df[['Age','Sex']].apply(male_female_child,axis=1)

# Clean up NaN values
deck = titanic_df['Cabin'].dropna()

# Define if passengers were alone or with a family and add it to the dataframe
titanic_df['Alone'] =  titanic_df.Parch + titanic_df.SibSp

titanic_df['Alone'].loc[titanic_df['Alone'] >0] = 'With Family'
titanic_df['Alone'].loc[titanic_df['Alone'] == 0] = 'Alone'

# Add new column to dataframe defining if the passenger survived or died
titanic_df["Survivor"] = titanic_df.Survived.map({0: "no", 1: "yes"})

# Render final products showing how age, sex, embark location, deck location,
# being alone and class affected survival rates 
generations=[10,20,40,60,80]

sns.lmplot('Age','Survived',hue='Sex',data=titanic_df,palette='winter',x_bins=generations)

sns.lmplot('Age','Survived',hue='Pclass',data=titanic_df,palette='winter',x_bins=generations)

sns.lmplot('Age','Survived',hue='Embarked',data=titanic_df,palette='winter',x_bins=generations)

sns.lmplot('Age','Survived',hue='Cabin',data=titanic_df,palette='winter',x_bins=generations)

sns.lmplot('Age','Survived',hue='Alone',data=titanic_df,palette='winter',x_bins=generations)