import time


def delay(seconds: int, func):
    # time.sleep(5)  # https://prnt.sc/eeTWseF75cmj
    time.sleep(seconds)
    return func()


def get_data():
    return {"data": "json"}


def print_info_world():
    print("Hello, world!")


if __name__ == '__main__':
    print(delay(3, get_data))
    delay(2, print_info_world)

