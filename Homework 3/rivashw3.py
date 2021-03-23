#!/usr/bin/python3
import sys
import pickle

class Dictions:
    def __init__(self, mydict, c, bigrams):
        self.unigrams = mydict
        self.bigrams = bigrams
        self.words = c

perfect = pickle.load(open('pickled_data2.dat', 'rb'))

#perfect.unigrams
perfect.bigrams
#perfect.words


typed = input('What do you wish to say: ')

#creating lists
deletion = []
insertion = []
transpose = []
substition =[]

j = set('abcdefghijklmnopqrstuvwxyz')

#functions for transpose

#functions for deletions
def deletions(word):
    for i in word:
        for letter in j:
            bi = i + letter
            if bi in perfect.bigrams:
                deletion.append(bi)


deletions(typed)
print('The Deletion\n\n' deletion, '\n')

#functions for insertions
def insertions(word):
    for i in word:
        word = word[1:]
        bi = word[0] + word[2]
        if bi in perfect.bigrams:
             insertion.append(bi)
        if len(word) == 3:
            break

insertions(typed)
print('The Insertion\n\n',insertion, '\n')

#functions for substitions
def substitions(word):
    for i in word:
#        word = word[1:]
        bi = word[0] + word[1]
        for letter in j:
            replace1 = bi[0].replace(bi[0], letter)
            replace2 = bi[1].replace(bi[1], letter)
            word = word[1:]
            if replace1 in perfect.bigrams:
                substition.append(replace1)
            if replace2 in perfect.bigrams:
                substition.append(replace2)
            if len(word) == 1:
                break

substitions(typed)
print('The Substition\n\n', substition, '\n')
