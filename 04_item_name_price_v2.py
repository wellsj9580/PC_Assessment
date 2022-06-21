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
def number_checker(question): 

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
  item_price = number_checker (" Item Price:$")