from unittest import mock

from bank_account import BankAccount

# мы не хотим отправлять настоящие деньги просто для проверки кода
# поэтому весь функционал нужно замокать


@mock.patch("bank_api.bank_api.transfer")
def test_should_transfer_request(mocked_transfer):
    mocked_transfer.return_value = "Mock"  # if pay returns a value
    test_account = BankAccount("My account", 100)

    test_account.pay("Other account", 50)
    # после pay проверяем что был вызван transfer
    mocked_transfer.assert_called_once_with(
        "My account",
        "Other account",
        50
    )
