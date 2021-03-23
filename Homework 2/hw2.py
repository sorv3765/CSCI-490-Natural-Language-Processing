#!/usr/bin/python3
import sys
from collections import defaultdict
from math import log

text = open(sys.argv[1],'r', encoding = 'iso‑8859‑1')

count = 0
dict_count = 0

#counting the number of arguements
count = len(sys.argv)
print("Number of arguements: {:7}".format(count), '\n')

alpha = set("abcdefghijklmnopqrstuvwxyz")
symbol =set("'-")
doubleHyphen = set("--")
#create my dict here
mydict = defaultdict(int)

#run with it function
def runWith(text):
    with open(sys.argv[1],'r', encoding = 'iso‑8859‑1') as text:
        for line in text:                  #for loop read line by line
            line = line.replace('--', '  ')
            for ch in line:
                if ch.lower() not in alpha and symbol:
                    line = line.replace(ch, ' ')

#counting the frequency of each letters in the file
def frequency(text):
    with open(sys.argv[1],'r', encoding = 'iso‑8859‑1') as text:
        for line in text:                           #for each line
            newline =line.split()
            for word in newline:
                for character in word:
                    character =character.lower()
                    if character in alpha:
                        if character in mydict:
                            mydict[character] += 1
                        else:
                            mydict[character] = 1

#sorted by key(alphabet)
def sortCharactersBychar():
    import operator
    for x,y in sorted(mydict.items(), key=operator.itemgetter(0)):
        print('{:1s}{:1s}{:9d}'.format(x,':', y))

#experiment this
#def experiment():
    


#sorted by biggest to smallest values using reverse
def sortCharactersByValue():
    import operator
    for x,y in sorted(mydict.items(), key=operator.itemgetter(1), reverse=True):
        print('{:1s}{:1s}{:9d}'.format(x,':', y))

len_dict = defaultdict(int)

#counting the length of each word in the file
def lengthOfWord(text):
    with open(sys.argv[1],'r', encoding = 'iso‑8859‑1') as text:
        for line in text:                           #for each line
            line = line.replace('--', '  ')
            for ch in line:
                if ch.lower() not in alpha and symbol:
                    line = line.replace(ch, ' ')
                    newline = line.split()
            for word in newline:
                len_word = len(word)
                if len_word in len_dict:
                    len_dict[len_word] += 1
                else:
                    len_dict[len_word] = 1



#printing the length of words
def printLength():
    import operator
    for x,y in  sorted(len_dict.items(), key=operator.itemgetter(0)):
        print('{:2d}{:1s}{:9d}'.format(x,':', y))

#Printing my Freaking Table
def printTable():
    import operator

    numbered = 0

    for x,y in sorted(len_dict.items(), key=operator.itemgetter(1), reverse=True):
        numbered +=1

        print('{:2d}'.format(numbered) , x, y, x*y, numbered*y, round( (log(x, 2)/log(y, 2)), 2) )


runWith(text)
frequency(text)

print('These are sorted by characters\n')
sortCharactersBychar()

print('\nThese are sorted by the largest values\n')
sortCharactersByValue()

lengthOfWord(text)

print('\nSorting by the length of words\n')
printLength()

print('\n')
print('Printed Tables\n')
printTable()

text.close()
