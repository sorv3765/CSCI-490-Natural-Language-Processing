#!/usr/bin/python3
import sys
import time
import pickle
from collections import Counter
from string import punctuation

#start
starting1 = time.perf_counter()
starting2 = time.process_time()
#stopped
stopping1 = time.perf_counter()
stopping2 = time.process_time()

print('start at elapsed time:\t',starting1,'\t','cpu time\t',starting2)
print('finished reading at elapsed time:\t',stopping1,'\t','cpu time\t',stopping2)
print('total elapsed time',(stopping1-starting1), '\tcpu time', (stopping2-starting2))

#opening the file to read it and count numbers of words"
count_words = 0
char_count = 0
mydict = {}
bigrams = {}
alpha = set("abcdefghijklmnopqrstuvwxyz<>")
symbol = set("<>")

#function to check for non-ascii characters
def nonascii(line):
    for char in line:
        if ord(char) > 127:
            char.replace(' ')
    return line

#function for bigram
def bigram(word):
    if len(word) > 1:
        if '<'+word[0] in bigrams:      #just added
            bigrams['<'+word[0]] += 1
        else:
            bigrams['<'+word[0]] = 1
        if word[-1]+'>' in bigrams:
            bigrams[word[-1]+'>'] += 1
        else:
            bigrams[word[-1]+'>'] = 1
        for character in word.lower():
            my_bigrams = word[0:2]
            if my_bigrams.isalpha():
                if my_bigrams in bigrams:
                    bigrams[my_bigrams.lower()] += 1
                else:
                    bigrams[my_bigrams.lower()] = 1
                word = word[1:]   #slice through word
                if len(word) == 2:
                    if word[1] in alpha:
                        if my_bigrams in bigrams:
                            bigrams[my_bigrams.lower()] += 1
                        else:
                            bigrams[my_bigrams.lower()] = 1
                        break

#function that sort the bigram
def sortBi():
    import operator
    for x,y in sorted(bigrams.items(), key=operator.itemgetter(0)):
        print('{:1s}{:1s}{:9d}'.format(x,':', y))

#function to get  every words in line
def wordcount(line):
    global count_words
    for word in line.split():
        bigram(word)
    words = line.split()
    count_words += len(words)
################################################

c = {}

with open(sys.argv[1], 'r') as f:
    for line in f:
        wordcount(line)
        for word in line.lower().split():
            key = word.rstrip(punctuation)
            if key in c:
                c[key] += 1
            else:
                c[key] = 1

print('Number of words:\t', count_words)
print('Number of distinct words:\t', len(c))

#counting the frequency of each letters in the file
def frequency():
    with open(sys.argv[1],'r', encoding = 'iso‑8859‑1') as text:
        for line in text:                           #for each line
            newline =line.split()
            for word in newline:
                word = '<'+word+'>'
                for character in word:
                    character = character.lower()
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

frequency()
sortCharactersBychar()

sortBi()

class Dictions:
    def __init__(self, mydict, c, bigrams):
        self.unigrams = mydict
        self.bigrams = bigrams
        self.words = c

data = Dictions(mydict, c, bigrams)

output3 = open("pickled_data2.dat", 'wb')
pickle.dump(data, output3)

