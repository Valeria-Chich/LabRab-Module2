BOOKS_DATABASE = [
    {
        "id_": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id_": 2,
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
        self.id_ = id_
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

    def __str__(self):
        return f'Книга "{self.name}"'
    """
    Возвращение питоновской строки названия через атрибут name.
    
    Пример:
    >>> str(Book("Геология")
    """

    def __repr__(self):
        return f'Book(id_={self.id_!r}, name={self.name!r}, pages={self.pages!r})'
    """
    Возвращие валидной питоновской строки.
    """

if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id_"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
