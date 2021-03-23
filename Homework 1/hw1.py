#!/usr/bin/python3
import sys
from decimal import Decimal

input1= "pride.txt"
input2= "swann.txt"

file1 = open(input1, "r")
file2 = open(input2, "r")

vowels = set("AEIOUaeiou\u00e9\u00e2\u00ea\u00ee\u00f4\u00fb\u00e0\u00e8\u00f9\u00eb\u00ef\u00fc\u00c0\u00c8\u00cc\u00d2\u00d9\u0152\u0153")
cons = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ\u00e7\u00c7\u0178\u00ff")
space = set(" ")
spec = set(".,?!;:<<>>$#%'")

countV1 = 0
countC1 = 0
countW1 = 0
countSS1 = 0
countS1 = 0
numlines1 = 0

for c in file1.read():
    c = c.lower()
    if c in vowels:
        countV1 += 1
    elif c in cons:
        countC1 += 1
    elif c in space:
        countSS1 += 1
    elif c in spec:
        countS1 += 1



with open(input1, "r") as l:
    for line in l:
       numlines1 +=1

with open(input1, "r") as file:
	text = file.read()
	chars = sum(len(word) for word in text)

vowelper = Decimal((countV1/(countV1+countC1))*100)
percent = round(vowelper,2)

print("Book: ", "pride.txt")
print("Number of lines	= {:7}".format(numlines1))
print("Number of characters = {:7}".format(chars))
print("Number of vowels	= {:7}".format(countV1))
print("Number of consonants = {:7}".format(countC1))
print("Number of letters = {:7}".format(countV1+countC1))
print("% vowel = {:7}".format(percent), " %")
print("\n\n\n")

countV2 = 0
countC2 = 0
countS2 = 0
countSS2 = 0
numlines2 = 0

for c in file2.read():
    c = c.lower()
    if c in vowels:
        countV2 += 1
    elif c in cons:
        countC2 += 1
    elif c in space:
        countSS2 += 1
    elif c in spec:
        countS2 += 1

with open(input2, "r") as l:
    for line in l:
       numlines2 +=1

with open(input2, "r") as file2:
        text2 = file2.read()
        chars2 = sum(len(word) for word in text2)

vowelper2 = Decimal((countV2/(countV2+countC2))*100)
percent2 = round(vowelper2,2)

print("Book: ", "swann.txt")
print("Number of lines = {:7}".format(numlines2))
print("Number of characters = {:7}".format(chars2))
print("Number of vowels = {:7}".format(countV2))
print("Number of consonants = {:7}".format(countC2))
print("Number of letters = {:7}".format(countV2+countC2))
print("% vowels = {:7}".format(percent2), "%")

print("\n\nActual: ")
print("Book		Consonants	Vowels")
print("pride.txt	",countC1,"	", countV1)
print("swann.txt	",countC2,"	", countV2)

row1 = 0
row2 = 0
rowtatol = 0
column1 = 0
column2 = 0
columntotal = 0
N = 0

expect1 = 0
expect2 = 0
expect3 = 0
expect4 = 0

part1 = 0
part2 = 0
part3 = 0
part4 = 0

totalexpect = 0

box1 = countC1
box2 = countV1
box3 = countC2
box4 = countV2

row1 = box1+box2
row2 = box3+box4
rowtotal = row1+row2 
column1 = box1+box3
column2 = box2+box4
columntotal = column1+column2
N = rowtotal


expect1 = round( (column1/N)*row1, 2)
expect2 = round( (column2/N)*row1, 2)
expect3 = round( (column1/N)*row2, 2)
expect4 = round( (column2/N)*row2, 2)

part1 = ((box1-expect1)**2)/expect1
part2 = ((box2-expect2)**2)/expect2
part3 = ((box3-expect3)**2)/expect3
part4 = ((box4-expect4)**2)/expect4

totalexpect = round(part1+part2+part3+part4, 2)

print("\n\nExpected:")
print("Book		Consonants	Vowels")
print("pride.txt	", expect1,"	", expect2)
print("swann.txt	", expect3,"	", expect4)

print("\n\n")
print("chi-square = ", totalexpect)
