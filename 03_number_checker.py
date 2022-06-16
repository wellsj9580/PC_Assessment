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

# Get price of the item 
  item_price = num_checker (" Item Price:$")