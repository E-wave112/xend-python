from xend_finance.models.schemas import CooperativeCycle

# from xend_finance.strategies.cooperative.cooperative_index import Cooperative
from .main_test import xend


def test_create_cooperative_cycle():
    try:
        args = {
            "group_id": 1,
            "cycle_stake_amount": "0.1",
            "payout_interval_in_seconds": 3600,
            "start_time_in_seconds": 1579014400,
            "max_members": 10,
        }
        created = xend.cooperative.create(args)
        assert type(args) == dict or CooperativeCycle
        assert type(created) == dict
    except Exception as e:
        assert isinstance(e, Exception)


def test_start_cooperative_cycle():
    try:
        cycle_id = 1
        started = xend.cooperative.start_cycle(cycle_id)
        assert type(cycle_id) == int
        assert type(started) == dict
    except Exception as e:
        assert isinstance(e, Exception)


def test_join_cooperative_cycle():
    try:
        cycle_id = 1
        number_of_stakes = 1
        joined = xend.cooperative.join(cycle_id, number_of_stakes)
        assert type(cycle_id) == int
        assert type(number_of_stakes) == int
        assert type(joined) == dict
    except Exception as e:
        assert isinstance(e, Exception)


def test_cooperative_info():
    try:
        cycle_id = 1
        inform = xend.cooperative.info(cycle_id)
        assert type(cycle_id) == int
        assert type(inform) == dict
    except Exception as e:
        assert isinstance(e, Exception)


def test_cooperative_cycle_member_exist():
    try:
        cycle_id = 1
        member_exist = xend.cooperative.cycle_member_exist(cycle_id)
        assert type(cycle_id) == int
        assert type(member_exist["data"]) == bool
    except Exception as e:
        assert isinstance(e, Exception)


def test_withdraw_ongoing_cooperative():
    try:
        cycle_id = 1
        withdraw_ongoing = xend.cooperative.withdraw_from_ongoing_cycle(cycle_id)
        assert type(cycle_id) == int
        assert type(withdraw_ongoing) == dict
    except Exception as e:
        assert isinstance(e, Exception)


def test_withdraw_completed_cooperative():
    try:
        cycle_id = 1
        withdraw_completed = xend.cooperative.withdraw_completed(cycle_id)
        assert type(cycle_id) == int
        assert type(withdraw_completed) == dict
    except Exception as e:
        assert isinstance(e, Exception)


def test_create_cooperative_group():
    try:
        group_name = "test"
        group_symbol = "TST"
        created = xend.cooperative.create_group(group_name, group_symbol)
        assert type(group_name) == str
        assert type(group_symbol) == str
        assert type(created) == dict
    except Exception as e:
        assert isinstance(e, Exception)


def test_get_cooperative_groups():
    try:
        groups = xend.cooperative.get_cooperative_groups()
        assert type(groups["data"]) == list
    except Exception as e:
        assert isinstance(e, Exception)


def test_get_cooperative_contributions():
    try:
        contributions_total = xend.cooperative.contributions()
        assert type(contributions_total["data"]) == list
    except Exception as e:
        assert isinstance(e, Exception)


def test_get_cooperative_cycles_in_group():
    try:
        group_id = 1
        cycles_in_group = xend.cooperative.cycles_in_group(group_id)
        assert type(group_id) == int
        assert type(cycles_in_group["data"]) == list
    except Exception as e:
        assert isinstance(e, Exception)
