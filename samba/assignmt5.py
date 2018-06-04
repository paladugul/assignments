#!user/dell/python

#5. take a string from the user and check contains only digits or not?

input1= raw_input("Enter a string : ")

if input1.isdigit():
	print "It contains only numeric characters"
else:
	print "It contains alphanumeric characters"




output:

Enter a string : 123456
It contains only numeric characters

Enter a string : python1234
It contains alphanumeric characters
