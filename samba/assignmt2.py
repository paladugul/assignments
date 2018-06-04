#!user/dell/python

#2. write a program to chek given substring is there in actual string or not? (search should be case insensitive)

a=raw_input("Enter a String: ")
b=raw_input("Enter Sub String: ")

def string1(a,b):
	a.lower()
	b.lower()
   	if b in a:
   		print "Substring is in actual string"
   	else:
   		print "Substring not found"
string1(a,b)



output:

Enter a String: welcome to HYd
Enter Sub String: HYd
Substring is in actual string
