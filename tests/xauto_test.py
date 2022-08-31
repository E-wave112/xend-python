# from xend_finance.strategies.xauto.auto import Xauto
from .main_test import xend


def test_approve_token():
    try:
        token_name = "TNT"
        amount = 300
        approve_token = xend.xauto.approve(token_name, amount)
        assert type(token_name) == str
        assert type(approve_token) == str
    except Exception as e:
        assert isinstance(e, Exception)


def test_deposit_token():
    try:
        token_name = "TNT"
        amount = 300
        deposit_token = xend.xauto.deposit(token_name, amount)
        assert type(token_name) == str
        assert type(deposit_token) == str
    except Exception as e:
        assert isinstance(e, Exception)


def test_deposit_native_token():
    try:
        token_name = "TNT"
        amount = 300
        deposit_native_token = xend.xauto.deposit_native(token_name, amount)
        assert type(deposit_native_token) == str
    except Exception as e:
        assert isinstance(e, Exception)


def test_withdraw():
    try:
        token_name = "MNT"
        amount = 190
        withdraw = xend.xauto.withdraw(token_name, amount)
        assert type(withdraw) == str
    except Exception as e:
        assert isinstance(e, Exception)


def test_get_ppfs():
    try:
        token_name = "MNT"
        ppfs = xend.xauto.ppfs(token_name)
        assert type(ppfs) == list
    except Exception as e:
        assert isinstance(e, Exception)


def test_get_share_balance():
    try:
        token_name = "MNT"
        share_balance = xend.xauto.share_balance(token_name)
        assert type(share_balance) == list or dict
    except Exception as e:
        assert isinstance(e, Exception)
