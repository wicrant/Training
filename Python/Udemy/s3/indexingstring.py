#Indexing example
mystring = "Hello World"
print (mystring)
print (mystring[0]) #Print the first letter in the string
print (mystring[-1]) # Print the last letter in the string
print (mystring[-3]) # Print the 3rd letter from right in the string

#Slicing example
mystring = "abcdefghijk"
print (mystring)
print (mystring[0:])  # Print 0th to end of string
print (mystring[3:])    #Print 3rd to end of string
print (mystring[:4]) #Print 0 to 3 characters from string
print (mystring[3:6]) #Print 3rd to 5th character from string
print (mystring[::]) #Print entire string
print (mystring[::2]) # Print alternate characters. Step size of 2
print (mystring[2:7:2]) #Print from 2 to 7 with step size of 2
print (mystring[::-1]) # Reverse the string
print (mystring[::-2])

