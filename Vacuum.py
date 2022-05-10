def Vacuum():
      cost = 0
  
location_input = input("Enter Location of Vacuum:")
status_input = int(input("Enter status of " + location_input + "(0 if clean/1 if dirty):"))
status_input_complement = int(input("Enter status of other room:"))
  
if location_input == 'A':
    print("Vacuum is placed in Location A")
    if status_input == 1:
        print("Location A is Dirty.")
        cost += 1
        print("Cost for CLEANING A " + str(cost))
        print("Location A has been Cleaned.")
      
        if status_input_complement == 1:
            print("Location B is Dirty.")
            print("Moving right to the Location B. ")
            cost += 1
            print("COST for moving RIGHT" + str(cost))
            cost += 1
            print("COST for SUCK " + str(cost))
            print("Location B has been Cleaned. ")
        else:
            print("No action" )
            print("Location B is already clean.")
        
    if status_input == 0:
      print("Location A is already clean ")
      if status_input_complement == 1:
        print("Location B is Dirty.")
        print("Moving RIGHT to the Location B. ")
        cost += 1
        print("COST for moving RIGHT " + str(cost))
        cost += 1
        print("Cost for SUCK " + str(cost))
        print("Location B has been Cleaned. ")
      else:
        print("No action ")
        print("Location B is already clean.")
        
    else:
      print("Vacuum is placed in location B")
      if status_input == 1:
        print("Location B is Dirty.")
        cost += 1
        print("COST for CLEANING " + str(cost))
        print("Location B has been Cleaned.")
        
        if status_input_complement == 1:
          print("Location A is Dirty.")
          print("Moving LEFT to the Location A. ")
          cost += 1
          print("COST for moving LEFT" + str(cost))
          cost += 1
          print("COST for SUCK " + str(cost))
          print("Location A has been Cleaned.")
        else:
          print("No action " + str(cost))
          print("Location A is already clean.")
          
      else:
        print(cost)
        print("Location B is already clean.")
        
        if status_input_complement == 1:
          print("Location A is Dirty.")
          print("Moving LEFT to the Location A. ")
          cost += 1
          print("COST for moving LEFT " + str(cost))
          cost += 1
          print("Cost for SUCK " + str(cost))
          print("Location A has been Cleaned. ")
          
        else:
          print("No action ")
          print("Location A is already clean.")
          
print("Total Cost: " + str(cost))

Vacuum()
