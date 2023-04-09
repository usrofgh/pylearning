alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
correct = "ZABCDEFGHIJKLMNOPQRSTUVWXYzabcdefghijklmnopqrstuvwxy"


def one_down(txt: str) -> str:
    return (
        "Input is not a string"
        if type(txt) != str
        else txt.translate(str.maketrans(alpha, correct))
    )
