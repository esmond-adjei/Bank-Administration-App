from datetime import datetime
from string import punctuation
from account import Account
from operations import *
from customer import Customer


# Create dummy accounts
    # - Account namename
    # - account number
    # - account type
    # - initial deposit
# Create dummy customers (note: not all users with accounts are customers)

account_db = {}

def get_fullname():
    '''Returns a fullname in a list'''
    print("Enter first name")
    first_name = get_name()

    print("Enter surname")
    surname = get_name()

    print("Enter other name or leave blank")
    other_name = get_name()
    return [first_name, surname, other_name]
def make_account_id(prefix='DT'):
    code = str(datetime.today())
    for l in code:
        if l in punctuation:
            code = code.replace(l,'')
    code = code.split()
    code = str(int(code[0])+int(code[1]))
    return code


# fullname = get_fullname
# acc_1 = Account(fullname,  )
make_account_id()