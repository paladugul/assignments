
def push_stack(contents):
    
    if len(stack) >= limit:
        print 'Your Stack is Overflow'
    else:
        stack.append(contents)
    print 'Stack after Push',stack
def pop_stack():
    if len(stack) <= 0:
        print 'Stack Underflow!'
        return 0
    else:
        return stack.pop()
if __name__=="__main__":
    stack = []
    limit = input('Enter the no of elements to be stored in stack :')
    for t in range(limit):
        contents = input('Enter element '+str(t)+' :')
        push_stack(contents)
    for t in range(limit):
        print 'Popping '+str(limit-t)+'th element:',pop_stack()
        print 'Stack after Popping!',stack
		

# output:

# Enter the no of elements to be stored in stack :5
# Enter element 0 :25
# Stack after Push [25]
# Enter element 1 :14
# Stack after Push [25, 14]
# Enter element 2 :36
# Stack after Push [25, 14, 36]
# Enter element 3 :56
# Stack after Push [25, 14, 36, 56]
# Enter element 4 :5
# Stack after Push [25, 14, 36, 56, 5]
# Popping 5th element: 5
# Stack after Popping! [25, 14, 36, 56]
# Popping 4th element: 56
# Stack after Popping! [25, 14, 36]
# Popping 3th element: 36
# Stack after Popping! [25, 14]
# Popping 2th element: 14
# Stack after Popping! [25]
# Popping 1th element: 25
# Stack after Popping! []
