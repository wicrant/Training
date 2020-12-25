#! /usr/bin/python3

# Chapter 19 - Print Formatting with Strings

print ("this is a string {}".format("INSERTED"))
print ("The {} {} {}".format("quick", "brown", "fox"))

print ("The {2} {0} {1}".format("quick", "brown", "fox"))

print ("The {2} {2} {2}".format("quick", "brown", "fox"))

print ("The {f} {q} {b}".format(f="fox", b="brown", q="quick"))

print ("The {f} {f} {f}".format(f="fox", b="brown", q="quick"))

result = 22/7
print ("The value of PI is {}".format(result))
print ("The value of PI is {r}".format(r=result))
print ("The value of PI is {r:1.5f}".format(r=result))

name ="Vikrant"
print ("Hello.. My name is {}".format(name)) #Use format
print (f"Hello.. My name is {name}") #Use f strigs to interset in a string
age = 40
print (f"{name} is {age} years old")





