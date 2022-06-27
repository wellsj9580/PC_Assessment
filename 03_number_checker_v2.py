# Function starts 

# Checks to make 
def number_checker(question, low, exit_code = None):

    error = "Please enter a number that is more than {}".format(low)
    
    while True:

        #  Get user response (as text)
        response = input(question)

        # if exit code is entered, end function and return code
        if response == exit_code:
            return response

        # check that user response is a number more than the minimum specified
        try:
            response = float(response)

            if response > low:
                return response

            else:
                print(error)

        except ValueError:
            print(error)

# Main routine starts here

# Asks for the price of the item 
user_choice = ""
while user_choice != "xxx":
    user_choice = number_checker("Enter a number more than zero", 0, "xxx")
    print("You chose", user_choice)
