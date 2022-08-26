## INPUT FUNCTIONS
def get_name():
    '''reads user name input, checks validity and returns the valid name.'''
    
    name = input("BT>>Enter your name: ").strip().capitalize()
    # check if is name is all letters and hiphens
    while not ('-'  in name and name.isalpha()):
        print("Name should be made of letters only\nTry again...\n")
        name = input("BT>>Enter your name: ").capitalize()
    return  name

def get_amount():
    '''Reads user amount input, checks validity and returns the valid amount.
       Checks if input IS DIGIT and allows FOR DECIMAL
    '''
    amount = input("BT>>Enter your amount: ")

    # check if amount is all numbers
    while not ('.' in amount or amount.isdigit()):
        print("Amount should be numbers only\nTry again...\n")
        amount = input("BT>>Enter your amount: ").capitalize()
    return  round(float(amount),2)

def select_service(services):
    '''allows user to select category of service and returns service.
       Checks if choice is INTEGER and if choise is IN RANGE.
    '''
    cat_service = services
    
    selection = -1
    while True:
        try:
            selection = int(input("BT>> Select a number: "))
            if selection in range(1,len(cat_service.keys())+1):
                return selection
            else:
                print("Choice out of range\n")
        except ValueError:
            print("Input should be an integer\n")
            continue


# ===================================================== #
# myName = get_name()
# print(f"Hello {myName}!")

# myAmount = get_amount()
# print(f"You entered GHS {myAmount}")

# services = {
#         '1': 'Deposit',
#         '2': 'Transfer',
#         '3': 'Withdraw',
#         '4': 'Borrow'
#     }

# choice = select_service(services)
# print(f"You chose {choice}")