# Function goes here 

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

# main routine goes here 
item_price = num_checker (" Item Price:$")
