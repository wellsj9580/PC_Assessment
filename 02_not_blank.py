# Checks to make sure a name is entered 
def not_blank (question):
  valid = False
  while not valid:
    response = input (question)

    if response !="":
        return response
    else:
        print ("Please enter the name of the item" )

# Get name of the item
item_name = not_blank (" Item Name: ")
