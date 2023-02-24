# Типы наследования: Multi-Level Inheritance, Multiple Inheritance, Hierarchical Inheritance, Single. and Hybrid Inheritance

class Dog:
    def __init__(self, name: str, bread: str) -> None:
        self.name = name
        self.bread = bread

dog1 = Dog("name1", "bread1")
dog2 = Dog("name2", "bread2")

# print(dog1 < dog2) # same like  - dog1.__lt__(dog2) - TypeError: '<' not supported between instances of 'Dog' and 'Dog
print(dog1.__lt__(dog2))  # NotImplemented. Так как этот метод не имплементирован
print(str(dog1))  # Выведет <__main__.Dog object at 0x00000221AB8C8910>
# Почему __str__ имплементирован, а __lt__ нет?
# Методы наследуются от object экз. класса. Там str имплементирован выводом ячейки памяти,
# а __lt__ имплементирован как возврат NotImplemented. Достаточно просто переопределить его и задать свою реализацию
      
