def read_from_file(file_name: str) -> list[str]:
    with open(file_name, "r") as file:
        return sorted([word.lower() for word in file.read().split() if word[0] in "wW"])


print(read_from_file("fn.txt"))
