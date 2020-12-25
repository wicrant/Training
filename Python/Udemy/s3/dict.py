#! /usr/bin/python3
#Chapter 23 Dictionaries in Python

# Dictionaries have a key value pair

# Dictionaries - Objects retrived by Key name. Unordered and cannot be sorted. Curly braces 
# Lists - Objects retrived by location. Ordered sequence can be indexed or sliced. square braces 

price = {'apple': 100, 'mango': 230, 'banana': 50}
print (price['apple'])

#dict can contain different data tyes, list and even dictionaries 

d = {'k1':123, 'k2':[0,1,2,3],'k3':{'insidekey':100} }   #This dict contains number, list and another dict. 


print (d['k1'])
print (d['k2'])
print (d['k2'][2])                  # fetch from a list in a dictionary
print (d['k3']['insidekey'])        # reading a nested dictionary

newdict = {'key1':['a', 'b','c']}
print (newdict['key1'][2].upper())  #Covert to a letter in a list in a dictory to upper case and print it. 
print (newdict)                     # Value is not stored in dictionary 

# Add new key value pair to dictionary

price ['papaya'] = 60               #Add new key value pair to ane exisiting dictionary
print (price)
price ['apple'] = 105               #Edit value of an existing key in the dictionary 
print (price)
                                    
print (price.keys())                 # Calling keys of a dictionary
print (price.values())               # Calling values of a dictinary   
print (price.items())               # Calling items of a dictionary


