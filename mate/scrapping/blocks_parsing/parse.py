import requests


def main():
    response = requests.get(
        "https://www.amazon.com/",
        headers={
            "user-agent":
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
        }
    )
    print(response.status_code)
    print(response.content)  # как сайт понимает что я не юзера браузер:
    # 1. Самая частая проблема - headers. requests.get указывает в headers что запрос от python(автоматически)
    # ![](headers.png) - тут их куча. Но чаще всего проблема в user-agent. При автоматизации:
    print(response.request.headers)  # 'User-Agent': 'python-requests/2.28.1'. - поменяй на нормальный


if __name__ == '__main__':
    main()