'''
Document Search Engine V.1
    A interactive TF/IDF document search engine using the Spark framework. 

Coded By: Tyler Linne
Date: 4/28/16
'''

from pyspark import SparkConf, SparkContext
from pyspark.mllib.feature import HashingTF
from pyspark.mllib.feature import IDF

# Configure Spark
conf = SparkConf().setMaster("local").setAppName("SparkTFIDF")
sc = SparkContext(conf = conf)

# Load documents to search through 
searchData = sc.textFile("c:/System/User Name/Folder Name/subset-small.tsv")
searchFields = searchData.map(lambda x: x.split("\t"))
documents = searchFields.map(lambda x: x[3].split(" "))

# Store the document names
docNames = searchFields.map(lambda x: x[1])

# Hash the words in each document to their TF
hashingTF = HashingTF(100000)  
tf = hashingTF.transform(documents)

# Compute TF*IDF 
tf.cache()
idf = IDF(minDocFreq=2).fit(tf)
tfidf = idf.transform(tf)

# Take user input 
# index a sparse vector 
search_item = input("What would you like to search for? ")
inputTF = hashingTF.transform([search_item])
inputHashValue = int(inputTF.indices[0])

# Extract TF*IDF score
# Get a new RDD for each document:
searchRelevance = tfidf.map(lambda x: x[inputHashValue])

# Zip in the document names 
zippedResults = searchRelevance.zip(docNames)

# Print the document with the maximum TF*IDF value:
print ("The best document for" + search_item + "is:")
print zippedResults.max()
