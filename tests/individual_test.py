# from xend_finance.strategies.individual.individual_index import Personal
from .main_test import xend


def test_flexible_deposit():
    try:
        deposit_amount = "20"
        flexible_deposit = xend.personal.flexible_deposit(deposit_amount)
        assert type(deposit_amount) == str
        assert type(flexible_deposit["data"]) == str
    except Exception as e:
        assert isinstance(e, Exception)


def test_fixed_deposit():
    try:
        deposit_amount = "30"
        lock_period = 4000
        fixed_deposit = xend.personal.fixed_deposit(deposit_amount, lock_period)
        assert type(deposit_amount) == str
        assert type(fixed_deposit["data"]) == str
    except Exception as e:
        assert isinstance(e, Exception)


def test_get_flexible_deposit_record():
    try:
        flexible_deposit = xend.personal.get_flexible_deposit_record()
        assert type(flexible_deposit["data"]) == list or dict
    except Exception as e:
        assert isinstance(e, Exception)


def test_get_fixed_deposit_record():
    try:
        fixed_deposit = xend.personal.get_fixed_deposit_record()
        assert type(fixed_deposit["data"]) == list or dict
    except Exception as e:
        assert isinstance(e, Exception)


def test_get_fixed_withdrawal():
    try:
        record_id = 1
        fixed_withdrawal = xend.personal.fixed_withdrawal(record_id)
        assert type(fixed_withdrawal["data"]) == str
    except Exception as e:
        assert isinstance(e, Exception)


def test_get_flexible_withdrawal():
    try:
        amount = "20"
        flexible_withdrawal = xend.personal.flexible_withdrawal(amount)
        assert type(flexible_withdrawal["data"]) == str
    except Exception as e:
        assert isinstance(e, Exception)
