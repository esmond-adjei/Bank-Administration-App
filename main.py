# START
import account, operations, tellerQueue, customer

## CREATE CUSTOMER
## - customer joins outside queue
customer1 = account.Account('esmond')
customer1.name = 'esmond'
print(customer1.name)



## ENQUEUE CUSTOMER
## - check customer service
## - enqueue to teller queue

## SERVE CUSTOMER
## - run account operation based on service required