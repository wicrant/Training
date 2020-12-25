#! /usr/bin/python3
#Chapter 28 I/O with Basic Files in Python

myfile = open('myfile.txt')         #Open a file
print (myfile.read())               # Read the file
print ("read file again")
print (myfile.read())               #reading file again doesn't return anything
print ('add myfile.seek(0)')
myfile.seek(0)                      #call seek(0) to change the cursor to 0th position of the file. 
print ("read file after seek(0)")
print (myfile.read())               # Reading again returns the file. 
myfile.seek(0)

myfile.readlines()                  # Read lines from the file. 

myfile.close()                  #Close the file after opening it

print ("Using with statement ---\n")

with open('myfile.txt') as my_new_file:
    contents = my_new_file.read()
    print (contents)

with open('my_new_file.txt',mode ='r') as f:
    print (f.read())

with open('my_new_file.txt',mode='a') as f:
    f.write('\nFOUR ON FOURTH')
with open('my_new_file.txt', mode ='r') as f:
    print (f.read())

with open('somefile.txt',mode='w') as f:
    f.write('Some text in somefile.txt')

with open('somefile.txt',mode='r') as f:
    print(f.read())


