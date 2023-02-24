class User:
    def __init__(
            self,
            name: str,
            surname: str,
            age: int,
            is_staff: bool,
            is_admin: bool
    ) -> None:
        self.name = name
        self.surname = surname
        self.age = age
        self.is_staff = is_staff
        self.is_admin = is_admin

    def get_info(self) -> str:
        return f"{self.name} {self.surname} (age: {self.age})"

    def get_staff_info(self) -> str:
        return f"is_staff: {self.is_staff}, is_admin: {self.is_admin}"

    def get_json_data(self) -> dict:
        return {
            "name": self.name,
            "surname": self.surname,
            "age": self.age,
            "is_staff": self.is_staff,
            "is_admin": self.is_admin
        }
