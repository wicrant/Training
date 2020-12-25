#!/usr/bin/python3
#Chapter 21 Lists in Python

my_list = [1,2,3]
my_list = ["String", 1, 3.14,"text as string"]  #Lists can contain different data types 

print (my_list[0])   #Read elements from lists
print (my_list[1:]) # LIst slicing (same as strings)

mylist = ["one", "two", "three"]
anotherlist = ["four", "five"]

print (mylist + anotherlist) #Concatenate Lists 
print ("Concatenate Lists elements = "+ mylist[0] + anotherlist[0]) #Concatenate lists  elements 

#Unlike strings, LISTS are mutable

newlist = mylist + anotherlist  #Concatenate lists 
print (newlist)                 #Print new list
newlist[0] = "ONE ALL CAPS"     #Mutate/Change element 0 of the list
print (newlist)                 #Print the new list

newlist.append("six")           # Append to a list
print (newlist)
newlist.append ("seven")        #Append one more
print (newlist)

newlist.pop()                   # Remove the last element from a list
print (newlist)

poppeditem = newlist.pop()
print (poppeditem)
print (newlist)

newlist.pop(0)                  # POP index item 0
print (newlist)

# Sort Lists 
charlist = ["a", "s","d", "f"]
numlist = [1,5,6,4,7,8,0,3,9]
print (charlist.sort())          #sORTS list but doesn't return anything. Sort modifies the source list itself
print (charlist)
numlist.sort()
print (numlist)

numlist.reverse()               # Reverse a list
print (numlist)
charlist.reverse()
print (charlist)


