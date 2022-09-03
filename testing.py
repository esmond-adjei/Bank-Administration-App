# Import the required libraries
from tkinter import *
from tkinter import font

# Create an instance of tkinter frame or window
win = Tk()

# Set the size of the window
win.geometry("700x350")

# Create two frames in the window
greet = Frame(win)
order = Frame(win)

# Define a function for switching the frames
def change_to_greet():
   order.pack_forget()
   greet.pack(fill='both', expand=1)

def change_to_order():
   greet.pack_forget()
   order.pack(fill='both', expand=1)

# Create fonts for making difference in the frame
font1 = font.Font(family='Georgia', size='22', weight='bold')
font2 = font.Font(family='Aerial', size='12')

# Add a heading logo in the frames
label1 = Label(greet, text="Hey There! Welcome to TutorialsPoint.", foreground="green3", font=font1)
label1.pack(pady=20)

label2 = Label(order, text="Find all the interesting Tutorials.", foreground="blue", font=font2)
label2.pack(pady=20)

# Add a button to switch between two frames
btn1 = Button(win, text="Switch to Greet", font=font2, command=change_to_order)
btn1.pack(pady=20)

btn2 = Button(win, text="Switch to Order", font=font2, command=change_to_greet)
btn2.pack(pady=20)

win.mainloop()

# # from account import Account
# from operations import get_fullname, select_cartegory
# from customer import *
# from tellerQueue import TellerQueue
# import json



# # load text file
# with open('client-database.txt', 'r+') as db:
#     for line in db.readlines():
#         # data = db.readline()
#         jsdb = json.dumps(line)
# print(jsdb)


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


# # ============================================== #
# CREATE THE ACCOUNT
## -- collect account info
# fullname = get_fullname()
# acc_type = {
#     '1':'Savings',
#     '2':'Student',
#     '3':'Work',
# }
# account_type = select_cartegory(acc_type)
# acc_1 = Account(fullname,account_type)
# data = acc_1.export_data()
# with open('client-database.txt','a') as db:
#     db.write(f"\n{data}")

# ============================================== #
# print("CREATE CUSTOMER")
# services = {
#     '1':'Deposit',
#     '2':'Transfer',
#     '3':'Withdraw',
# }
# cust_1 = Customer(get_fullname(), select_cartegory(services))
# cust_1.set_priority(True)
# cust_1.issue_ticket()
# print(cust_1)

# # ============================================== #
# print("CREATE TELLER QUEUE")
# que_1 = TellerQueue(make_account_id('T'), get_fullname(), select_cartegory(services))
# que_1.enqueue(cust_1)
# length = que_1.current_queue_size()
# print(que_1)
