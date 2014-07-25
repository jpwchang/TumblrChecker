#tumblrchecker.py
#Automatically generates tumblr address by concatenating random
#words, then checks to see if the address exists
#2014 Jonathan Chang

import sys
import random
import urllib2
import webbrowser
from bs4 import BeautifulSoup

#safely request a number from the user
def getNumWordsFromUser():
    result = 0
    while result <= 0:
        userIn = raw_input("Please specify number of words to use: ")
        try:
            result = int(userIn)
            if result <= 0:
                print "Error: Input is not a positive number. Please reenter:"
        except ValueError:
            print "Error: Input is not a positive number. Please reenter:"
            result = 0
    return result

#pick howMany random words and concatenate them together
def randwords(howMany):
    #open the common words list
    commonWords = open("commonwords", "r")
    #store the common words in a list for easy access
    commonList = []
    for word in commonWords:
        commonList.append(word)
    commonWords.close()
        
    #open the (full) word list
    words = open("words", "r")
    #store the words in a list for easy access
    wordlist = []
    for word in words:
        wordlist.append(word)
    words.close()
    
    result = "http://"
    #randomly pick words. 75% chance of picking from list of most
    #common words, 25% chance of picking from full list
    for i in range(howMany):
        diceRoll = random.randint(1, 100)
        if diceRoll <= 25:
            index = random.randint(0, len(wordlist)-1)
            result += wordlist[index].rstrip('\r\n')
        else:
            index = random.randint(0, len(commonList)-1)
            result += commonList[index].rstrip('\r\n')

    return result

#main function
if __name__ == '__main__':
    numWords = 0
    #try to get number or words from command line arguments
    if len(sys.argv) > 1:
        try:
            numWords = int(sys.argv[1])
        except ValueError:
            print "Error: Input is not a positive number. Please reenter:"
            numWords = getNumWordsFromUser()
    #otherwise, prompt user for number of words
    else:
        numWords = getNumWordsFromUser()

    random.seed()

    #open the word list
    words = open("words", "r")

    #generate an address
    address = randwords(numWords)

    #append ".tumblr.com"
    address += ".tumblr.com"

    print "Testing address: " + address

    #connect to the url
    try:
        conn = BeautifulSoup(urllib2.urlopen(address))
        print address + " exists!"
        yn = raw_input("Would you like to visit it (y/n)?")
        if yn.lower() == 'y' or yn.lower() == 'yes':
            webbrowser.open(address)
    except:
        print address + " does not appear to exist"

