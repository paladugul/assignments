
#27,31 Take some single digit numbers from the user and findout min, maximum, sum, average

num=input("Enter total numbers of digits:")
l=[]
for i in num:
        x=input("Enter digit")
        l.append(i)
print "Minimum of given values:",min(l)
print "Maximum of given values:",max(l)
print "Sum of given values:",sum(l)
avg=sum(l)/len(l)
print "Avg of given numbers:",avg

# output:

# Enter total numbers of digits:5,2,4,6,3,8
# Enter digit4
# Enter digit3
# Enter digit8
# Enter digit6
# Enter digit5
# Enter digit2
# Minimum of given values: 2
# Maximum of given values: 8
# Sum of given values: 28
# Avg of given numbers: 4
