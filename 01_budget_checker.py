# Function goes here

def budget_checker(question): 

  error = "The minimum is $5 "

  valid = False 
  while not valid: 

    # Ask user for number and check it is valid
    try: 
      response = float(input(question))

      if response <= 4.99 :
        print (error)
        break 
      else:
        return response 

 # If a number is not entered then display an error 
    except ValueError: 
      print (error)

# main routine goes here 
budget = budget_checker("What is your budget?: ")
print("Your Budget: ", budget)


        
  