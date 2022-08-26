from select import select
from account import Account
from operations import get_fullname, select_cartegory
from customer import *


# Create dummy accounts
    # - [x] account name
    # - [x] account number
    # - [x] account type
    # - [x] initial deposit
# Create dummy customers (note: not all users with accounts are customers)
    # - [x] customer full name
    # - [x] customer service demand
    # - [x] assign priority
# Add customer to queue
    # - [] create queue
    # - [] check if customer has an account (give option to create account false)
    # - [] issue ticket
    # - [] add to queue

## CREATE THE ACCOUNT
### -- collect account info
# fullname = get_fullname()
# acc_type = {
#     '1':'Savings',
#     '2':'Student',
#     '3':'Work',
# }
# account_type = select_cartegory(acc_type)
# ### -- create account
# new_account = Account(fullname, account_type)
# ### --- save account info permanently
# data = new_account.export_data()
# with open('bank-database.txt', 'a') as db:
#     db.write(f"\n{data}")


# =================================================== #
## MAKE CUSTOMER
services = {
    '1':'Deposit',
    '2':'Transfer',
    '3':'Withdrawal',
}
cust_1 = Customer(get_fullname(), select_cartegory(services))
cust_1.set_priority(True)
print(cust_1)