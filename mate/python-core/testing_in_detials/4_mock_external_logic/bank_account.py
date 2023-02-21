from bank_api_test_coverage import bank_api


class BankAccount:
    def __init__(
            self,
            account_number: str,
            balance: int
    ) -> None:
        self.account_number = account_number
        self.balance = balance

    def pay(self, to_number: str, amount: int) -> None:
        if amount < 0:
            raise ValueError("Amount can't be negative")
        if amount > self.balance:
            raise ValueError("Not enough money")

        response = bank_api.transer(self.account_number, to_number, amount)
        print("RESPONSE: ", response)

