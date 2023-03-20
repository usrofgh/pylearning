class bank_api:
    @staticmethod
    def transfer(sender, receiver, amount: float) -> str:
        sender.balance -= amount
        receiver.balance += amount

        return "Done"
