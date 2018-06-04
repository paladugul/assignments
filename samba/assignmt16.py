#! user/dell/python

# 16. Take the input from the user for(Total number of people, toatl number of busses, Number of seats for bus). Based on the input
# 	Decide whether there is sufficient busses or not and give solution for how many extra busses required.

import math

no_of_people = input("Enter No.of People: ")
no_of_buses = input("Enter No.of of busses: ")
no_of_seats = input("Enter No.of seats: ")

tot_no_seats = no_of_buses*no_of_seats

if no_of_people > tot_no_seats:
	print "Seats not sufficient so we need extra buses"
	extra_people = float(no_of_people-tot_no_seats)
	extra_bus = extra_people/no_of_seats
	bus = math.ceil(extra_bus)
	print "The extra no.of buses required is:{}".format(bus)

else:
	print "Seats are sufficient"



output:

Enter No.of People: 450
Enter No.of of busses: 6
Enter No.of seats: 35
Seats not sufficient so we need extra buses
The extra no.of buses required is:7.0

Enter No.of People: 500
Enter No.of of busses: 5
Enter No.of seats: 100
Seats are sufficient
