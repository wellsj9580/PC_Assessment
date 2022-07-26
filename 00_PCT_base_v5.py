#import pandas

# Function goes here 

# Asks for instructions 
def yes_no (question):

  error = "Please answer yes/no"

  valid = False 
  while not valid: 

    # ask question and put response in lowercase 
    response = input(question).lower()

    if response == "yes" or response == "y":
      print ("Please enter your budget and Name, Price and weight in gram/ml of your items, At the end of the program it will recommend the best item!  ")
      return "yes"
    elif response == "no" or response == "n":
      return "no"
    else:
        print (error)

# Checks for an interger more than 5
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

# Checks to make sure a number is entered 
def num_checker (question):

  error = "Please enter the price of the item  "
  
  vaild = False 
  while not vaild:

  # ask user for number and check it is valid 
    try: 
      response = float (input(question))

      if response <= 0 :
          print (error)
      else:
        return response 
        
      # if an interger is not entered, display and error 
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
def weight_checker (question):

  error = "Please enter a number more than 50g/ml  "
  
  vaild = False 
  while not vaild:

  # ask user for number and check it is valid 
    try: 
      response = float (input(question))

      if response <= 49.99 :
          print (error)
      else:
        return response 
        
      # if an interger is not entered, display and error 
    except ValueError: 
      print (error)

# Changes price of items to currency 
def currency(x):
  return "${:.2f}".format(x)

# *** Main routine goes here ***

# Asks for instructions 
instructions_ = yes_no("Would you like to read instructions? ")

# Asks for the budget  
get_budget = budget_checker ("What is your budget?: $")

# Set up dictionaries and lists 
item_list= []
price_list = []
weight_gmml = []
weight_kgl = []
unit_price = []

variable_dict = {
  "Item": item_list,  
  "Price": price_list,
  "gm/ml": weight_gmml,
  "kg/l": weight_kgl,
  "Unit Price": unit_price
}

# Loop to get name, price and weight 
item_name = ""
while item_name.lower() != "xxx":

  print ()
  # Get name, price and weight of the item 
  item_name = not_blank (" Item name: ")
  if item_name.lower() == "xxx":
    break
  
  # Asks for price of item
  price = num_checker(" Item Price:$" )

  # Asks for weight of item in gm/ml
  weight_gm = weight_checker(" Item Weight(G/ML): ") 
  
  # Converts weight in gm/ml to kg/l
  weight_kg = weight_gm / 1000

  # Calculates the unit price  
  unit = price / weight_kg  

  # Add item, price, weight and unit ptice to list  
  item_list.append(item_name)
  price_list.append(price)
  weight_gmml.append(weight_gm)
  weight_kgl.append(weight_kg)
  unit_price.append(unit)

expenses_frame = pandas.DataFrame (variable_dict)
expenses_frame = expenses_frame.set_index('Item')



# *** Printing area ***

print()
print("*** Overwiew ***")
print()
print("Your Budget: $", get_budget)
print()
# Prints data Frame 
print (expenses_frame)
print()
# Recommendation 
print("*** Recommendation *** ")
print()
print(expenses_frame.loc[expenses_frame['Unit Price']==expenses_frame['Unit Price'].min(),:])