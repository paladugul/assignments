#! user/dell/python

#18. Determine the factors of a number entered  by the user

num=input("Enter a number to find factorial:")
factorial = 1
# check if the number is negative, positive or zero
if num < 0:
   print "Sorry, factorial does not exist for negative numbers"
elif num == 0:
   print "The factorial of 0 is 1"
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print "The factorial of",num,"is",factorial


output:

Enter a number to find factorial:-3
Sorry, factorial does not exist for negative numbers

Enter a number to find factorial:0
The factorial of 0 is 1

Enter a number to find factorial:5
The factorial of 5 is 120


