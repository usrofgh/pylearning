def square_color(string: str, rank: int) -> str:
    if rank % 2 == 0:
        if ord(string) % 2 == 0:
            return "black"
        return "white"

    if ord(string) % 2 == 0:
        return "white"
    return "black"



def square_color(string: str, rank: int) -> str:
    return "white" if (ord(string) + rank) % 2 else "black"
