import pandas 

# Function goes here 

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

  error = "Please enter the price of the item  "
  
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

def currency(x):
  return "${:.2f}".format(x)

# Main routine goes here 
get_budget = budget_checker ("What is your budget?: $")


def get_item(var_fixed):

  # set up dictionaries and lists 
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
    
    price = num_checker(" Item Price:$" )

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
  

  # Currency formatting (uses currency function)
  add_dollars = ['Price', 'Unit Price']
  for item in add_dollars: 
    expenses_frame[item] = expenses_frame[item].apply(currency)


  return [expenses_frame]
\

# Main routine goes here 
 
variable_expenses = get_item("variable")
variable_frame = variable_expenses


  # *** Printing area *** 
print()
print(variable_frame)
print()



