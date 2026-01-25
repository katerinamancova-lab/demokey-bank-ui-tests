import pytest
from pages.transfer_page import TransferPage

@pytest.mark.auth_data("testuser", "password")
def test_transfer_by_account_success(browser, auth_user):
    transfer_page = TransferPage(browser)
    transfer_page.open("/bank/transfer")

    transfer_page.transfer_by_account(
        account_number="220012345678",
        amount="10"
    )

    transfer_page.wait_visible(transfer_page.SUCCESS_MESSAGE)
