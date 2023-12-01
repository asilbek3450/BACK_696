class Book:
    def __init__(self, nomi, avtor, janr):  # initial
        self.title = nomi
        self.author = avtor
        self.genre = janr
        self.copies = 1

    def get_copy(self):
        pass

    def return_copy(self):
        pass


# Kitoblar yaratish (o'zbekcha
book1 = Book("Sariq devni minib", "Xudoyberdi To'xtaboyev", "sarguzasht")
book2 = Book("O'tkan kunlar", "Abdulla Qodiriy", "drama")


class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        if book.title not in self.books:
            self.books[book.title] = [book]
        else:
            return f"Bunday kitob mavjud"

    def list_books(self):
        for book in self.books:
            print(f"{book} - {self.books[book][0].copies} ta")


# Kutubxona yaratish
library = Library()

# Kutubxonaga kitoblar qo'shish
library.add_book(book1)
library.add_book(book2)

print(
    "Bo'limni tanlang:\n 1. Kitoblar ro'yxati\n 2. Kitob olish \n 3. Kitob qaytarish \n 4. Kitoblar qo'shish \n 5. Chiqish")

while True:

    choice = input("Tanlang: ")
    if choice == "1":
        library.list_books()
    elif choice == "2":
        library.list_books()
        title = input("Kitobni tanlang: \n")
        if title in library.books:
            library.books[title][0].get_copy()
            print("Kitob olindi")
        else:
            print("Bunday kitob yo'q")
    elif choice == "3":
        library.list_books()
        title = input("Kitob nomini kiriting: ")
        if title in library.books:
            library.books[title][0].return_copy()
            print("Kitob qaytarildi")
    elif choice == "4":
        library.list_books()
        title = input("\nYangi kitob nomini kiriting: ")
        author = input("Kitob muallifi: ")
        genre = input("Kitob janri: ")
        library.add_book(Book(title, author, genre))
        print("Kitob qo'shildi")
    elif choice == "5":
        print("Dastur tugadi")
        break
    else:
        print("Noto'g'ri tanlov")
