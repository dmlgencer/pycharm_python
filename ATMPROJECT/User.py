
class User:
    def __init__(self, name, account):
        self.name = name
        self.account = account

    def displeyUserInformations(self):
        print(f"Kullanıcı: {self.name}")
        self.account.check_balance()