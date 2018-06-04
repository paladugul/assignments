
# 27. Take some single digit numbers from the
# user and findout min, maximum, sum, average

dig=input("enter single digit numbers to find out min,max,sum,avg")

for i in dig:
    k=len(str(i))
      
    if k!=1:
        print "Enter single digits only"
        break
else:
    a=min(dig)
    b=max(dig)
    c=sum(dig)
    d=c/len(dig)
    print "Min is %d\nMax is %d\nSum is %d\nAvg is %d"%(a,b,c,d)
    

# output:

# enter single digit numbers to find out min,max,sum,avg2,5,6,8,7,3
# Min is 2
# Max is 8
# Sum is 31
# Avg is 5