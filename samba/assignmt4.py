#!user/dell/python

#4. take a number from the user and check whether it is prime?

number = int(input("Enter any number: "))
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")
else:
    print(number, "is not a prime number")



output:

Enter any number: 7
(7, 'is a prime number')

Enter any number: 10
(10, 'is not a prime number')

Enter any number: -1
(-1, 'is not a prime number')
