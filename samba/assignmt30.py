"""
30. Take actuual string, soucrce string, destination string.
replce first nth occurances of soucestring with
destination string of actual string
"""
str1=raw_input("Enter the actual string")
source_str=raw_input("Enter the sub string ")
dest_str=raw_input("Enter the destination string")
for i in str1:
    if source_str in str1:
        k = str1.replace(source_str,dest_str)
print "Replaced string is:{}".format(k)
    
# output:

# Enter the actual stringarmstrong
# Enter the sub string arm
# Enter the destination stringhand
# Replaced string is:handstrong

