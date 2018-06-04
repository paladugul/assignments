#! user/dell/python

# 14. take a string from the user and check contains atleast one capital letter or not?

string1=raw_input("Enter a string to find it contains capital letter or not:")
for i in string1:
    if i==i.capitalize():
        print "string contains capital letters"
        break
else:
    print "string doesnot contains capital letters"


output:

Enter a string to find it contains capital letter or not:Welcome
string contains capital letters

Enter a string to find it contains capital letter or not:python
string doesnot contains capital letters
