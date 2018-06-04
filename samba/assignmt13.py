#! user/dell/python

#13. take a string from the user and check contains atleast one chars or not?

string1=raw_input("Enter a string:")
for i in string1:
    if i.isalpha():
        print "string contains characters"
        break
else:
    print "string doesnot contains characters"


output:

Enter a string:python123
string contains characters

Enter a string:1234q
string contains characters

Enter a string:123456
string doesnot contains characters


