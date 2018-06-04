#! user/dellpython

#12. take a string from the user and check contains atleast one alphabets or not?

string1=raw_input("Enter a string:")
for i in string1:
    if i.isalpha():
        print "string contains alphabets"
        break
else:
    print "string doesnot contains alphabets"



output:

Enter a string:pyton123
string contains alphabets

Enter a string:123456
string doesnot contains alphabets

