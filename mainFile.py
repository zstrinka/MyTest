'''
Created on Mar 13, 2017

@author: Zohar
'''
import Question1


#Option to remove punctuation from word count tools
removePunctuation = False

def main():
    print("Hello World!")
    wordDictionary = Question1.wordCounts(removePunctuation)
    numSentences = Question1.sentenceCounts()
    #Question1.descendingFrequency(removePunctuation) #Brownie option 3
    #print("Average sentence length: ", sum(wordDictionary.values())/numSentences) #Brownie option 1
    



if __name__ == '__main__':
    main()