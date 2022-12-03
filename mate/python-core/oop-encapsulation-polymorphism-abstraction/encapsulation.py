class Product:
    def __init__(
        self,
        name: str,
        price: int,
        last_customer_rating: float = None
    ):
        
        self.name = name
        self.price = price
        self.last_customer_rating = last_customer_rating

    def print_product_info(self):
        print(
            f"The {self.name} price is {self.price}"
            f" (rating: {self.last_customer_rating})"
        )


book = Product("Garri", 50, 5)
print(book.last_customer_rating)  # 5
book.last_customer_rating = 4.5
book.print_product_info()  # The Garri price is 50 (rating: 4.5)
book.name = None
print(book.name, '\n')  # None
# Кто угодно может изменить данные переменных обратившись к ним напрямую, для
# избежания этого нужна инкапсуляция



class Product:
    def __init__(
        self,
        name: str,
        price: int,
        last_customer_rating: float = None
    ):
        
        self.__name = name
        self.__price = price
        self.last_customer_rating = last_customer_rating

    def print_product_info(self):
        print(
            f"The {self.__name} price is {self.__price}"
            f" (rating: {self.last_customer_rating})"
        )

book = Product("Ara", 34, 5)
book.name = 1  # Имя не поменялось, просто добавился аттрибут
book.__name = 1  # Имя не поменялось. Просто добавился аттрибут
book.print_product_info()  # The Ara price is 34 (rating: 5)

print(book.__dict__)  # {'_Product__name': 'Ara', '_Product__price': 34,
# 'last_customer_rating': 5, 'name': 1, '__name': 1}

book._Product__name = 1  # хранится в _Product__name. Теперь изменили
book.print_product_info()  # The 1 price is 34 (rating: 5)

# В python инкапсуляция не такая строгая, используя её, всё равно можно изменить
