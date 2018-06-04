#! user/dell/python

#10. Show the below menu to the user until and until user select quit and display corresponding os message

'''
Menu:
1. windows
2. Linux
3. Mac
4. quit
'''

print "1.Windows\n2.Linux\n3.Mac\n4.Quit:"
while True:
	input1 = input("Enter any OS u want to perform : ")
	if input1==1:
		print "You selected Windows Operationg System"
	elif input1==2:
		print "You selected Linux Operationg System"
	elif input1==3:
		print "You selected Mac Operationg System"
	elif input1==4:
		print "you selected Quiting operation system"
		break
	else:
		print "selected wrong option"



output:

.Windows
2.Linux
3.Mac
4.Quit:
Enter any OS u want to perform : 1
You selected Windows Operationg System
Enter any OS u want to perform : 2
You selected Linux Operationg System
Enter any OS u want to perform : 3
You selected Mac Operationg System
Enter any OS u want to perform : 4
you selected Quiting operation system

1.Windows
2.Linux
3.Mac
4.Quit:
Enter any OS u want to perform : 5
selected wrong option
Enter any OS u want to perform : 4
you selected Quiting operation system
