#!user/dell/python

#6. take a string from the user and check contains only  alphabets or not?

input1= raw_input("Enter a string : ")

if input1.isalpha():
	print "It contains only alphabetic characters"
else:
	print "It contains alphanumeric characters"



output:

Enter a string : pythonrocks
It contains only alphabetic characters

Enter a string : python1234
It contains alphanumeric characters
