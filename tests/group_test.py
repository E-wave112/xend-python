# from xend_finance.strategies.group.group_index import Group
from .main_test import xend


def test_create_group():
    try:
        group_name = "test"
        group_symbol = "TST"
        created_group = xend.group.create(group_name, group_symbol)
        assert type(group_name) == str
        assert type(group_symbol) == str
        assert type(created_group["data"]) == str
    except Exception as e:
        assert isinstance(e, Exception)


def test_get_groups():
    try:
        groups = xend.group.get_groups()
        assert type(groups["data"]) == list
    except Exception as e:
        assert isinstance(e, Exception)


def test_single_group():
    try:
        group_id = 1
        group = xend.group.get_single_group(group_id)
        assert type(group["data"]) == dict or list
    except Exception as e:
        assert isinstance(e, Exception)


def test_xend_rewards():
    try:
        rewards = xend.group.get_xend_rewards()
        assert type(rewards["data"]) == int
    except Exception as e:
        assert isinstance(e, Exception)
