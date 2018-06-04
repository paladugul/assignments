#! user/dell/python

#8. take a string from the user and check contains only  capiatl letters or not?

input1= raw_input("Enter a string to check it contains capital letters or not: ")

if input1.isupper():
	print "All are in uppercase letters"
else:
	print "Not all are upper case letters"


output:

Enter a string to check it contains capital letters or not: ROCKS
All are in uppercase letters

Enter a string to check it contains capital letters or not: google
Not all are upper case letters

Enter a string to check it contains capital letters or not: Awesom
Not all are upper case letters
