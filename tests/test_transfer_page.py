from pages.transfer_page import TransferPage
import pytest
import time
import pytest

@pytest.mark.auth_data("testuser", "password")
def test_transfer_successfully(browser, auth_user):
    transfer_page = TransferPage(browser)
    transfer_page.open("/bank/transfer")
    transfer_page.transfer(recipient= "testuser", amount= "10")
    transfer_page.wait_for_exact_url("https://demoqa.ru/bank/transfer")
    assert browser.current_url == "https://demoqa.ru/bank/transfer"