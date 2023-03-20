from unittest import mock

import pytest

from bank_account import BankAccount


@pytest.fixture()
def mocked_transfer():
    with mock.patch("bank_api.bank_api.transfer") as mock_pay:
        yield mock_pay


def test_should_transfer_request(mocked_transfer):
    mocked_transfer.return_value = "Done"
    sender = BankAccount("Sender", 100)
    receiver = BankAccount("Receiver", 0)

    sender.pay(receiver, 10)
    mocked_transfer.assert_called_once_with(sender, receiver, 10)
