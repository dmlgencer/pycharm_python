
class Book:
    def __init__(self, book_name, author, year):
        self.book_name=book_name
        self.author=author
        self.year=year

    def display_info(self):
        print(f"Kitabın adı: {self.book_name}")
        print(f"Kitabın yazarı: {self.author}")
        print(f"Kitabın basım yılı: {self.year}")