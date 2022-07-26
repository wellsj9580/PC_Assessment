
def yes_no (question):

  error = "Please answer yes/no"

  valid = False 
  while not valid: 

    # ask question and put response in lowercase 
    response = input(question).lower()

    if response == "yes" or response == "y":
      print ("Please enter your budget and Name, Price and weight in gram/ml of your items, At the end of the program it will recommend the best item!  ")
    elif response == "no" or response == "n":
      return "no"
    else:
        print (error)


# main routine goes here
instructions_ = yes_no("Would you like to read instructions? ")

