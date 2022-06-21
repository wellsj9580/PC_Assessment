# Function goes here 

def gram_ml_checker(question, low, exit_code = None):

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

# Main routine 

# Gets the weight of the item in Grams/ML
item_weight = ""
while item_weight != "xxx":
    item_weight = gram_ml_checker(" Item Weight(G/ML): ", 49.99, "xxx")

