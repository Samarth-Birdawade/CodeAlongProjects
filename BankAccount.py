class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    @property
    def balance(self):
        print("@Property called")
        return self._balance
    
    @balance.setter
    def balance(self, amount):
        print(f"Process started to change balance to {amount}:")
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        self._balance = amount

    @balance.deleter
    def balance(self):
        del self._balance

if __name__ == '__main__':
    account = BankAccount("Samarth", 10000)
    print(account.balance)
    account.balance = 15000
    print(account.balance)

    try:
        account.balance = -500
    except Exception as e:
        print(f'{e}')