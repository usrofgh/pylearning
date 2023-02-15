# class Person:
#     def __init__(self, name: str, age: int) -> None:
#         self._name = name
#         self._age = age
#
#     def get_name(self) -> str:
#         return self._name
#
#     def set_name(self, name: str) -> None:
#         if name != "":
#             self._name = name
#         else:
#             raise ValueError("you don't write an empty value")
#
#     name = property(get_name, set_name)
#
#     @property
#     def age(self) -> int:
#         return self._age
#
#     @age.setter
#     def age(self, age: int) -> None:
#         self._age = age
#
#
# person = Person("Nikita", 19)
# print(person.name)
# print(person.age)
# person.name = "Oleg"
# person.age = 1
# print(person.name)
# print(person.age)
import string


# refactor this code


# refactor this code




# class CorrectMessage:
#     def __init__(self, message: str) -> None:
#         self.message = message
#
#     @property
#     def message(self) -> str:
#         return self._message
#
#     @message.setter
#     def message(self, message: str) -> None:
#         self._message = message.capitalize()
#
#
# correct_message = CorrectMessage("heLLO, wORlD!")
# print(correct_message.message)  # Hello, world!
#
# correct_message.message = "aNOther CoRREcT meSSAge"
# print(correct_message.message)  # Another correct message
#
# print(correct_message.__dict__)  # False
# # message is property, not an instance attribute


class Transaction:
    def __init__(
            self,
            amount: int,
            date: str,
            currency: str = "USD",
            usd_conversion_rate: float = 1.0,
            description: str = None
    ) -> None:
        self._amount = amount
        self._date = date
        self._currency = currency
        self._usd_conversion_rate = usd_conversion_rate
        self._description = description

    @property
    def amount(self) -> int:
        return self._amount

    @property
    def date(self) -> str:
        return self._date

    @property
    def currency(self) -> str:
        return self._currency

    @property
    def usd_conversion_rate(self) -> float:
        return self._usd_conversion_rate

    @property
    def description(self) -> str:
        if self._description is None:
            return "No description provided"
        return self._description

    @property
    def usd(self) -> float:
        return self._usd_conversion_rate * self._amount


transaction = Transaction(
    amount=2000,
    currency="UAH",
    usd_conversion_rate=0.035,
    date="17.08.2021",
    description="Some description"
)
print(
    transaction.date,                # 17.08.2021
    transaction.amount,              # 2000
    transaction.currency,            # UAH
    transaction.usd_conversion_rate, # 0.035
    transaction.usd,                 # 70.0 (2000 * 0.035)
    transaction.description,         # "Some description"
)
# transaction.description = "new"      # AttributeError: can't set attribute
