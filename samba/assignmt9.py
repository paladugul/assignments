#! user/dell/python

#9. take a string from the user and check contains only  small letters or not?

input1= raw_input("Enter a string to check it contains lowercase letters or not: ")

if input1.islower():
	print "All are in lowercase letters"
else:
	print "Not all are lower case letters"


output:

Enter a string to check it contains lowercase letters or not: google
All are in lowercase letters

Enter a string to check it contains lowercase letters or not: PYTHON ROCKS
Not all are lower case letters

Enter a string to check it contains lowercase letters or not: Windows
Not all are lower case letters

