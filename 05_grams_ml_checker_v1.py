# Function goes here 

# Function goes here

# Asks user for budget 
def budget_checker(question): 

  error = "Sorry, the minimum is $5 "

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


# Checks to make sure a name is entered 
def not_blank (question):
  valid = False
  while not valid:
    response = input (question)

    if response !="":
        return response
    else:
        print ("Please enter the name of the item" )

# Checks to make sure a number is entered 
def num_checker(question): 

  error = "Please enter the price of the item  "

  valid = False 
  while not valid: 

    # Ask user for number and check it is valid
    try: 
      response = float(input(question))

      if response <= 0 :
        print (error)
        break 
      else:
        return response 
        
 # If a number is not entered then display an error 
    except ValueError: 
      print (error)

def gram_ml_checker(question, low, exit_code = None):

    error = "Please enter a number that is more than {}".format(low)
    
    while True:

        #  Get user response (as text)
        response = input(question)

        # if exit code is entered, end function and return code
        if response == exit_code:
            return response

        # check that user response is a number more than the minimum specified
        try:
            response = float(response)

            if response > low:
                return response

            else:
                print(error)

        except ValueError:
            print(error)

# Main routine 

budget = budget_checker("What is your budget?: $")
print("Your Budget: $", budget)

# Loops to get name and price of item  
item_name = ""
while item_name.lower() != "xxx":

  print ()
  # Get name of the item
  item_name = not_blank (" Item Name: ")
  if item_name == "xxx":
      break

  # Get price of the item 
  item_price = num_checker (" Item Price:$")

# Gets the weight of the item in Grams/ML
item_weight = ""
while item_weight != "xxx":
    item_weight = gram_ml_checker(" Item Weight(G/ML): ", 49, "xxx")

