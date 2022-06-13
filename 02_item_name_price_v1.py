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

# Asks user for  the name and price of item 
def item_name (question):
  valid = False
  while not valid:
    response = input (question)

    if response !="":
        return response
    else:
        print ("Please enter the name of the item" )

def item_price(question): 

  error = "Please enter a number more than 0 "

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

budget = budget_checker("What is your budget?: $")
print("Your Budget: $", budget)
print()
item_name = item_name("Item Name: ")
item_price = item_price("Item Price: $")



