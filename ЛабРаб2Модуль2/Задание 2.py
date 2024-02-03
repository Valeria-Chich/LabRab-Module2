BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]

class Book:
    """
    Документация на класс.
    Класс описывает модель книги.
    """
    def __init__(self, id_: int, name: str, pages: int):
        self.id = id_
        self.name = name
        self.pages = pages
        """
        Создание и подготовка к работе объекта "Книга".

        :param id: идентификатор книги
        :param name: название книги
        :param pages: количество страниц в книге

        Пример:
        >>> book= Book(1, 'Геология', 343)
        """

class Library:
    """
    Документация на класс.
    Класс описывает модель библиотеки.
    """
    def __init__(self, books=None):
        if books is None:
            self.books = []
        else:
            self.books = books
        """
        Создание и подготовка к работе объекта "Библиотека".

        :param books=Non: необязательный аргумент со значением по умолчанию None

        """
    def get_next_book_id(self):
        if not self.books:
            return 1
        else:
            return self.books[-1].id + 1
        """
        Возвращение индентификатора для добавления новой книги в библиотеку.
        """
    def get_index_by_book_id(self, book.id):
        for i, book in enumerate(self.books):
            if book.id == book_id:
                return i
            raise ValueError("Книги с данным id не существует")
            """
            Возвращение индекса книги в списке, который хранится в атрибуте экземпляра класса.
            """


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
