import pandas

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

budget = budget_checker("What is your budget?: $")
print("Your Budget: $", budget)

def not_blank (question, error):
    
    valid = False
    while not valid:
      response = input (question)

      # If the name is not blank, program continues 
      if response == "":
          print ("{}. \n Please try agian.\n".format(error))
          continue 
  
      return response       

# Asks user for  the name and price of item 
def item_name (question):
  valid = False
  while not valid:
    response = input (question)

    if response !="":
        return response
    else:
        print ("Please enter the name of the item" )

item_name = item_name("Item Name: ")


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


item_price = item_price("Item Price: $")

# Loop to get component, quantity and price
item_name = ""
while item_name.lower() != "xxx":

  # set up dictionaries and lists 
  name_list = []
  price_list = []
  
  variable_dict = {
    "Item Name": name_list,  
    "Item Price": price_list
  }

  print ()
  # Get name, quantity and item
  item_name = not_blank ("Item name: ", "The item name can't be blank.")
  if item_name.lower() == "xxx":
    break
  
  item_price = not_blank ("Item Price: $", "The item price can't be blank.")
  if item_name.lower() == "xxx":
    break

  # Adds item and price to lists 
    name_list.append(item_name)
    price_list.append(item_price)
    
  data_frame = pandas.DataFrame (variable_dict)
  data_frame = data_frame.set_index('Item')
    
# Printing area
print ()
print("Your Budget: $", budget)
print ()

print ("Items ")
print ()
print (name_list)

print ()
print ("Price ")
print ()
print (price_list)
