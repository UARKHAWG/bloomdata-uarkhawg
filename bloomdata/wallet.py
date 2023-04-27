class Wallet:

    # 1st thing to run when we make a new class
    # outline required user-provided input values here
    def __init__(self, initial_amount=0):
        # save the user-provided initial_amount as an attribute
        # self refers to whatever object I'm working with
        self.balance = initial_amount

    # spend cash method
    def spend_cash(self, amount):
        if self.balance < amount:
            return "not enough money"
        self.balance -= amount
        return f'Remaining balance: ${self.balance}'

    #add cash method
    def add_cash(self, amount):
        self.balance += amount
        return f'New balance: ${self.balance}'


    # __repr__ method
    # changes how the 'object' looks when it is printed out
    # the presence of the self keyworld allows me to access or
    # modify class attributes within this function
    def __repr__(self):
        return f"Wallet with a balance of: ${self.balance}"   

if __name__ == '__main__':
    wallet1 = Wallet(1000)
    print(wallet1)
    print(wallet1.spend_cash(120))
    print(wallet1.spend_cash(1234))
    print(wallet1.balance)
    print(wallet1.add_cash(100))
    print(wallet1.balance)