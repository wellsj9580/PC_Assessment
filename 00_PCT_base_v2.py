# Import libraries

# *** Functions go here ***  

# Gets budget 
def budget_checker(question): 

  error = "Please enter a number that is more than 5 "

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
\

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


# *** Main routine goes here ***

# Asks user for budget
budget = budget_checker("What is your budget?: $")
print("Your Budget: $", budget)

# Asks user for name and price of profucts they want 

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

# Asks user for weight in grams 

# Converts weight in grams to weight in kg 

# Calculates the unit cost of the product 

# Find the remcommend product (based on tne buget)

# Instructions 