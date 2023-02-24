from bank_api import bank_api


class BankAccount:
    def __init__(
            self,
            account_number: str,
            balance: int
    ) -> None:
        self.account_number = account_number
        self.balance = balance

    def pay(self, receiver, amount: int) -> None:
        if amount < 0:
            raise ValueError("Amount can't be negative")
        if amount > self.balance:
            raise ValueError("Not enough money")

        response = bank_api.transfer(self, receiver, amount)
        print(response)
