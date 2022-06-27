# Function starts 

#checks fro an interger more than 0 
def budget_checker(question): 

  error = "The minimum is $5 "

  valid = False 
  while not valid: 

    # ask user for number and check it is valid
    try: 
      response = int(input(question))

      if response <= 4.99 :
        print (error)
      else:
        return response 

 # if an interger is not entered, display and error 
    except ValueError: 
      print (error)

# main routine goes here 
budget = budget_checker("What is your budget?: $")
print("Your Budget: $", budget)

        
  