from ATMPROJECT.Account import Account
from ATMPROJECT.User import User


class ATM:
    def __init__(self, user):
        self.user = user

    def menuGoruntuleme(self):
        print("1- Bakiye Sorgulama ")
        print("2- Para Çekme ")
        print("3- Para Yatırma ")
        print("4- Çıkış ")

    def bas(self):
        while True:
            self.menuGoruntuleme()
            sorgu = input("Lütfen yapmak istediğiniz işlemin numarasını tuşlayınız ")
            if sorgu=='1':
                self.user.account.check_balance()
            if sorgu=='2':
                amount = float(input("Çekmek istediğiniz miktarı girin: "))
                self.user.account.withdraw(amount)
            if sorgu=='3':
                amount = float(input("Yatırmak istediğiniz miktarı girin: "))
                self.user.account.deposit(amount)
            if sorgu=='4':
                print("Çıkış yapılıyor.....")
                break
            else:
                print("Geçersiz seçenek lütfen tekrar deneyiniz")

if __name__=="__main__": # kodun doğrudan çlaıştığını gösterir.
    hesap = Account("1234318", 10000.0)
    kullanici = User("Damla Gençer", hesap)
    atm = ATM(kullanici)
    atm.bas()
