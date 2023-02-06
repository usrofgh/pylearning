class Wallet:
    def __init__(self, brand: str, money_inside: int):
        self.brand = brand
        self.money_inside = money_inside

class User:
    def __init__(
            self,
            name: str,
            age: int,
            wallet: Wallet = None,
            best_friend = None
    ):
        self.name = name
        self.age = age
        self.wallet = wallet  # composition
        self.best_friend = best_friend

katia = User("Katia", 26)
john = User("John", 29)
sonia = User("Sonia", 36)

katia.best_friend = john
john.best_friend = sonia
sonia.best_friend = katia

katia.wallet = Wallet("Adidas", 0)

katia.best_friend.wallet = katia.wallet
katia.wallet = None

katia.best_friend.best_friend.wallet = katia.best_friend.wallet
katia.best_friend.wallet = None

katia.best_friend.best_friend.best_friend.wallet = katia.best_friend.best_friend.wallet
katia.best_friend.best_friend.wallet = None


print(katia.wallet.brand)