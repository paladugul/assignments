
# 21.Given an age, figure out whether someone's a baby, toddler, child, teenager, adult or older

year=input("Enter no of years:")
if year<=1:
    print "baby"
elif year in (2,4):
    print "toddler"
elif year in range(5,12):
    print "child"
elif year in range(13,19):
    print "teenager"
elif year in range(20,40):
    print "adult"
else:
    print "older"


# output:

# Enter no of years:1
# baby

# Enter no of years:5
# child

# Enter no of years:14
# teenager

# Enter no of years:38
# adult

# Enter no of years:48
# older