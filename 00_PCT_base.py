# Import libraries

# *** Functions go here ***  

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

# *** Main routine goes here ***

# Asks user for budget
budget = budget_checker("What is your budget?: ")
print("Your Budget: ", budget)

# Asks user for name and price of profucts they want 

# Asks user for weight in grams 

# Converts weight in grams to weight in kg 

# Calculates the unit cost of the product 

# Find the remcommend product (based on tne buget)

# Instructions 