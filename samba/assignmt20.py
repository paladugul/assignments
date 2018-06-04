#! user/dell/python

#20. Take two numbers from the user a,b check whether a is divisible by b or not?

a=input("Enter a value:")
b=input("Enter b value:")
if b==0:
    print "a is not divisable by b"
else:
    n=a/b
    print "a is divisable by b and result is",n


output:

Enter a value:10
Enter b value:0
a is not divisable by b

Enter a value:15
Enter b value:5
a is divisable by b and result is 3

