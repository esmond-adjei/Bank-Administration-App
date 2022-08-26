## ACCOUNT OBJECT
class Account:
    def __init__(self, account_name, account_id, account_type):
        self.name = account_name
        self.id = account_id
        self.type = account_type
        self.balance = 0

    def check_balance(self):
        return self.balance


## ACCOUNT SERVICES FUNCTIONS
def withdraw(amount, account, notify=True):
    balance = account.balance
    if balance and (balance - amount) > 0:
        balance = balance - amount
    else:
        # print(f"BT<< Withdrawal of GHS {amount} failed due to insufficient balance in account no: {account.name}\n")
        notification(0,withdraw,amount,account,notify)
        return 0
    account.balance = balance
    # print(f"BT<< Withdrawal GHS {amount} successful. {account.name} balance is GHS {account.balance}\n")
    notification(1,withdraw,amount,account,notify)
    return 1

def deposit(amount,account, notify=True):
    account.balance += amount
    # print(f"BT<< Deposit of GHS {amount} successful. {account.name} balance is GHS {account.balance}\n")
    notification(1,deposit,amount,account,notify)
    return 1

def transfer(sender_account, receiver_account, amount, notify=True):
    withdraw_result = withdraw(amount,sender_account,False)
    if withdraw_result:
        receiver_account.balance += amount
    print(f"\nBT<< Transfer of GHS {amount} from {sender_account.name} to {receiver_account.name}...")
    notification(withdraw_result,transfer,amount,sender_account)

def notification(success_value,function,amount,account,notify=True):
    '''Dynamically generates notifications depending on service rendered'''
    if notify:
        prep, status = (' of','Successful') if success_value else ('','Failed to')
        print(f"BT<< {status} {function.__name__}{prep} GHS {amount}. {account.name} balance is GHS {account.balance}")


# ========================================================== #
esmond = Account('Esmond','12345678','student')
osbert = Account('Osbee','98765432','enterprise')

deposit(1000,esmond)
withdraw(10,esmond)
transfer(esmond,osbert,1000)

print("\nEsmond account balance:", esmond.check_balance())
print("Osbee account balance:",osbert.check_balance())
