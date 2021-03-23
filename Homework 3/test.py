#!/usr/bin/python3

from collections import defaultdict

infile = open('ap88.txt', 'r')

word_frequency = defaultdict(int)

#mydict = {}

#letter_frequency['a'] = 123
#letter_frequency['b'] = 90

#print(letter_frequency['a'])

#a print function
def printdict(mydict):
    for key in mydict:			#each word in dict
        print( key, ": ", mydict[key])	#print each word with its value

#a process function... putting into dictionary
def process(myfile, mydict):
    for line in myfile:			#for each line
        newline = line.split()		#for each word in the line
        for word in newline:
            if word in mydict:		#if word matches in dict
                mydict[word] += 1	#count them
            else:
                mydict[word] = 1	#else its counted as 1

#process(infile, word_frequency)

printdict(word_frequency)
