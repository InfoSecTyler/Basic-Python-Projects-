'''
Hiring Decision Tool V.1
    A decision tree in the Spark framework aimed at helping managers assess
    applicants
    
Coded by: Tyler Linne
Date: 4/28/16
'''

# Import required tools 
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.tree import DecisionTree
from pyspark import SparkConf, SparkContext
from numpy import array

# Configure Spark
conf = SparkConf().setMaster("local").setAppName("SparkDecisionTree")
sc = SparkContext(conf = conf)

# Create functions that turn text data into numerical data 
def binary(YN):
    if (YN == 'Y'):
        return 1
    else:
        return 0

def mapEducation(degree):
    if (degree == "AS"):
        return 1
    elif (degree == 'BS'):
        return 2
    elif (degree =='MS'):
        return 3
    elif (degree == 'PhD'):
        return 4
    else:
        return 0

# Convert CSV file to a LabeledPoint
def createLabeledPoints(fields):
    yearsExperience = int(fields[0])
    employed = binary(fields[1])
    previousEmployers = int(fields[2])
    educationLevel = mapEducation(fields[3])
    privateSchool = binary(fields[4])
    stateSchool = binary(fields[5])
    topTier = binary(fields[6])
    interned = binary(fields[7])
    hired = binary(fields[8])

    return LabeledPoint(hired, array([yearsExperience, employed,
        previousEmployers, educationLevel, privateSchool, stateSchool, topTier,
        interned]))

#Load a CSV file of past canidates and filter out the header 
hireData = sc.textFile("c:/user/user name/file/hireinfo.csv")
header = hireData.first()
hireData = hireData.filter(lambda x:x != header)

# Split each line into a list 
csvData = hireData.map(lambda x: x.split(","))

# Convert lists to LabeledPoints
trainingData = csvData.map(createLabeledPoints)

# Create a test candidate
testCandidates = [ array([10, 1, 3, 1, 0, 1, 0, 0])]
testData = sc.parallelize(testCandidates)

# Train decisionTree classifier 
model = DecisionTree.trainClassifier(trainingData, numClasses=2,
                                     categoricalFeaturesInfo={1:2, 3:4, 4:2, 
                                     5:2, 6:2, 7:2},impurity='gini', maxDepth=7,
                                     maxBins=32)

# Get predictions
predictions = model.predict(testData)
print ('Hire prediction:')
results = predictions.collect()
for result in results:
    print result

# Print out the tree's path
print('Learned classification tree model:')
print(model.toDebugString())
