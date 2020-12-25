#! usr/bin/python3

#Chapter 17 - String Properties and Methods 

name = "Sam"
print ("Name is = " + name)
last_letters = name[1:]
print ("last letters are = " + last_letters) #Slice 1 to end
newname = 'P' + last_letters #Concatenate P to last_letters
print ("New name is = " + newname)

#Add Strings or Concatenate strings 
x = "Hello"
y = "World"
print (x +y)

print (x*3)

mystr = "Hello World"
print (mystr.upper())
print (mystr.lower())

# Split string
x = "Hi this is a string"
print (x.split())
print (x.split('i'))




