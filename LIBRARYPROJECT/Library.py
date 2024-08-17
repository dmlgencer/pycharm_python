
#kitap ekleme, kaldırmai listeleme olsun
class Library:
    def __init__(self):
        self.books=[]

    def add_book(self, book):
        self.books.append(book)
        print(f"{book.name} Kitap kütüphaneye eklendi")
        return


    def remove_book(self, book):

        self.books.remove(book)
        print(f"{book.name} Adlı kitap kütüphaneden silindi")
        return

    def list_of_library(self):
        if self.books:
            print("Kütühanedeki kitaplar: ")
            for book in self.books:
                book.display_info()
        else:
            print("Kütühanede hiç kitap yok")
