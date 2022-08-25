from actdetails import Account
from usdefinedexc import lowbalance_exception
def withdraw(balance,amount):
    try:
        if (balance == 0):
            return 'no balance'
        elif (balance < amount):
            return
    except(lowbalance_exception):
        return 'low balance error'
us1 = withdraw(100, 1000)
print(us1)

