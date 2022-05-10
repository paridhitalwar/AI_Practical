print ("""
This is the Monty Hall problem.
There are 3 doors in front of you, and there is a prize behind one of them.
Once you select a door, I will open one of the two you had not selected which does not have a prize behind it.
You will then have the opportunity to switch from the door you originally selected to an alternate door..
""")
import random


A = "A"
B = "B"
 
C = "C"


doors = ["A", "B", "C"]


prize = random.choice(doors)


selection = input("Select door 'A', 'B', or 'C': ")


print ("""
This problem relies on conditional probabilities.
It is suggested that you switch doors, you will have a higher probability of winning of you do.""")



if selection == prize:
    remaining = list(set(doors) - set(prize))
    open_door = random.choice(list(set(doors) - set(random.choice(remaining))))
    alternate = random.choice(list(set(doors) - set(open_door) - set(prize)))


else:
    open_door = random.choice(list(set(doors) - set(selection) -
    set(prize)))
    alternate = random.choice(list(set(doors) - set(open_door) - set(selection)))


print ("""
 
The door I will now open is: %r """ % open_door)

second_chance = input("Would you like to select the third door? Type 'Yes' or 'No': ")


if second_chance == "Yes": 
    print ("""
    The door you will switch to is: %r """ % alternate)


if alternate == prize: 
    print ("""
    Congrats, you win! The prize was behind the alternate, %r""" % alternate)
else:
    print ("""
    Sorry, the prize was behind the original door %r""" % prize)



if second_chance != "Yes": 
    print ("""
    You decided to keep your initial door, %r""" % selection) 
    if selection != prize:
        print ("""
        Sorry, the prize was behind the alternate door, %r""" % prize)
else:
    print("""
 
    Congrats, you win! The prize was behind your original selection, %r""" % selection)



print ("""
This is a check:""")


print ("Prize: %r" % prize)
print ("Selection: %r " % selection) 
print ("Alternate: %r " % alternate)
print ("Door opened: %r " % open_door)
