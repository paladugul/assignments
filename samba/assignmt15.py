#! user/dell/python

#15. take a string from the user and check contains atleast one small letter or not?

input1= raw_input("Enter a string to check it contains atleast one lowercase letters or not: ")

for i in input1:
	if i==i.lower() and i.isalpha():
		print "String contains lowercase letters"
		break
else:
	print "String doesnt contains lower case letters"


output:

Enter a string to check it contains atleast one lowercase letters or not: PYTHOn
String contains lowercase letters

Enter a string to check it contains atleast one lowercase letters or not: WELCOME
String doesnt contains lower case letters