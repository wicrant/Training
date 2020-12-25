#! /usr/bin/python3

#Chapter 25 Tuples with Python

#Tuples are similar to Lists but are immutable
# Tuple uses round brackets () vs. list uses square brackets [] vs. dictionary uses curly brackets {}

t = (1,2,3)
mylist = [1,2,3]

print (type(t))             #Returns type tuple
print (type(mylist))        #Return type list

print (len(t))              # Returns length of tuple 
print (len(mylist))         # Returns length of list 

tup = ('a', 'a', 'b')
print (tup.count('a'))
print (tup.index('b'))
print (tup[0])

print (set("Mississippi"))

