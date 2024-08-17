
class Account:
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance

    #hesaplama işlemleri
    def check_balance(self):
        print(f"Güncel bakiye: {self.balance} TL")


    def withdraw(self, amount):
        if amount <=self.balance and amount>0:
            self.balance -= amount
            print(f"{amount} TL para çekildi. Güncel bakiye: {self.balance} TL ")
        else:
            print("Geçersiz miktar.")


    def deposit(self, amount):
        if amount>0:
            self.balance += amount
            print(f"{amount} TL para yatırıldı. Güncel bakiye: {self.balance} TL")
        else:
            print("Geçersiz miktar.")


