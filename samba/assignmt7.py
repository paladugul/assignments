#!user/dell/python

#7. take a string from the user and check contains only  special chars or not?

input1=raw_input("Enter input to check it contains special characters or not :")
spchar="""~ ` ! @ # $ % ^ & * ( ) _ - + = [ ] { } | \ : ; " < > ? / . ,'"""
l=list(input1)

for i in input1:
    if i in spchar:
        print "All are special chars"
        break
    else:
        print "Not All are special chars"
        break



output:

Enter input to check it contains special characters or notjfkdjfijijk49384
Not All are special chars

Enter input to check it contains special characters or not@#$%^&**
All are special chars

Enter input to check it contains special characters or not :fjjfka!@%^%&(^)
Not All are special chars
