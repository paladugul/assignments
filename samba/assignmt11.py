#!user/dell/python

#11. take a string from the user and check contains atleast one digit or not?

# input1= raw_input("Enter a string :")

# for i in input1:
# 	if i.isdigit():
# 		print "It contains digits"
# 		break
# 	else:
# 		print "It doesn't contain digits"


string1=raw_input("Enter a string:")
for i in string1:
    if i.isdigit():
        print "string contains digits"
        break
else:
    print "string doesnot contains digits"


output:

Enter a string:welcome123
string contains digits

Enter a string:python
string doesnot contains digits




