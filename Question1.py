'''
Created on Mar 13, 2017

@author: Zohar
'''
import string
import re

def wordCounts(remPunctuation):
    countDoc = dict()
    with open ("Question1Text.txt", "r") as myfile:
        data=myfile.read()
        splitRow = data.split()
        if remPunctuation == True:
            x = [''.join(c for c in s if c not in string.punctuation) for s in splitRow]
        else:
            x = splitRow
        for word in x:
            if word in countDoc:
                countDoc[word]+=1
            else:
                countDoc[word]=1
    print("Total word count: ", sum(countDoc.values()))
    print("Unique words: ",len(countDoc))
    return countDoc
    
def sentenceCounts():
    # Much more sophisticated methods for handling this problem are available on 
    # this stackoverflow question: http://stackoverflow.com/questions/4576077/python-split-text-on-sentences
    countDoc = 0
    with open ("Question1Text.txt", "r") as myfile:
        data=myfile.read()
        splitData = filter(None, re.split(r"[.!\?] ", data))
        for sentence in splitData:
            #print(sentence) #Kept for debugging to check the output
            countDoc +=1
    print("Sentences: ", countDoc)
    return countDoc
    
def descendingFrequency(remPunctuation):
    dictionaryUnsorted = wordCounts(remPunctuation)
    sortedDict = sorted(dictionaryUnsorted, key=dictionaryUnsorted.get, reverse=True)
    for word in sortedDict:
        print(word)
    
    