print(25*2)
print(12/6)


import pandas

# Function goes here 

#checks for an interger more than 0 
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
    
# Checks to make sure a number is entered 
def weight_checker (question):

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

def list_maker (var_fixed):

  # Set up dictionaries and lists to hold data 
  name_list = []
  price_list = []
  unit_price_list = []
  item_weight_grml_list = []
  item_weight_kgl_list = []

  variable_dict = {
    "Item": name_list, 
    "Price": price_list,
    "Unit Price": unit_price_list,
    "Weight (gr/ml)": item_weight_grml_list,
    "Weight (kg/l)":item_weight_kgl_list  

  }
 
  # Loops to get name, price and weight of the item   
  item_name = ""
  while item_name.lower() != "xxx":

    print ()
    # Get name of the item
    if var_fixed == "variable":
      item_name = not_blank (" Item Name: ")
    if item_name == "xxx":
        break

    # Get price of the item 
    item_price = num_checker (" Item Price:$")

    # Gets the weight of the item in Grams/ML
    item_weight = weight_checker (" Item Weight(G/ML): ")

    # Add item, quantity and price to lists 
    name_list.append(item_name)
    price_list.append(item_price)
    unit_price_list.append()
    item_weight_grml_list.append(item_weight)
    item_weight_kgl_list.append()

  data_frame = pandas.DataFrame (variable_dict)
  data_frame = data_frame.set_index('Item')

  # Calculate the unit price 
  data_frame['Unit Price'] = data_frame['Price'] / data_frame ['Weight (gr/ml)']

# Main routine 

# main routine goes here 
budget = budget_checker("What is your budget?: $")
print("Your Budget: $", budget)

# Loops to get name, price and weight of the item
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
    item_weight = weight_checker (" Item Weight(G/ML): ")

print = list_maker