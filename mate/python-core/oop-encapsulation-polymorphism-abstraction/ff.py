class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def eat(self) -> None:
        print(f"{self.name} is eating")


class Cat(Animal):
    def sleep(self) -> None:
        print(f"{self.name} is sleeping")


    def eat(self) -> None:
        print(f"{self.name} drinks milk")


class Dog(Animal):
    def bark(self) -> None:
        print(f"{self.name} is barking")

    def eat(self) -> None:
        print(f"{self.name} is eating beacon")


class CatDog(Cat, Dog):
    def laught(self) -> None:
        print(f"{self.name} is laughing")


cat = Cat("cat")
dog = Dog("dog")
catdog = CatDog("catdog")

cat.eat()  # cat drinks milk
cat.sleep()  # cat is sleeping

dog.eat()  # dog is eating beacon
dog.bark()  # dog is barking

catdog.sleep()  # catdog is sleeping
catdog.bark()  # catdog is barking
catdog.laught()  # catdog is laughing
catdog.eat()  # catdog drinks milk
