
#24.Write a program to findout biggest number in the given numbers

def highest_num(n):
        l=[]
        for i in range(n):
                num=input("Enter number:")
                l.append(num)
        max1=l[0]
        for i in l:
                if max1 < i:
                        max1=i
        return max1
n=input("Enter total number of digits:")
x=highest_num(n)
print "The highest number in the given numbers:",x


# output:

# Enter total number of digits:4
# Enter number:5
# Enter number:6
# Enter number:7
# Enter number:8
# The highest number in the given numbers: 8
