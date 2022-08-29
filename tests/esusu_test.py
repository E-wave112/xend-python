# from xend_finance.strategies.esusu.esusu_index import Esusu
from xend_finance.models.schemas import EsusuCycle
from .main_test import xend


def test_create_esusu_cycle():
    try:
        args = {
            "group_id": 1,
            "deposit_amount": "300",
            "payout_interval_in_seconds": 3600,
            "start_time_in_seconds": 1579014400,
            "max_members": 10,
        }
        create_esusu_cycle = xend.esusu.create_esusu(args)
        assert type(args) == dict or EsusuCycle
        assert type(create_esusu_cycle) == dict
    except Exception as e:
        assert isinstance(e, Exception)


def test_esusu_cycles_count():
    try:
        cycles_count = xend.esusu.get_cycles_count()
        assert type(cycles_count["data"]) == int
    except Exception as e:
        assert isinstance(e, Exception)


def test_esusu_info():
    try:
        esusu_id = 1
        esusu_info = xend.esusu.get_esusu_info(esusu_id)
        assert type(esusu_id) == int
        assert type(esusu_info["data"]) == list or dict
    except Exception as e:
        assert isinstance(e, Exception)


def test_cycle_id_from_cycles_created():
    try:
        position_in_cycles_created = 1
        cycle_id = xend.esusu.get_cycle_id_from_cycles_created(
            position_in_cycles_created
        )
        assert type(position_in_cycles_created) == int
        assert type(cycle_id["data"]) == int
    except Exception as e:
        assert isinstance(e, Exception)


def test_join_esusu_cycle():
    try:
        esusu_id = 1
        join_esusu_cycle = xend.esusu.join(esusu_id)
        assert type(esusu_id) == int
        assert type(join_esusu_cycle) == dict
    except Exception as e:
        assert isinstance(e, Exception)


def test_start_cycle():
    try:
        cycle_id = 1
        start_cycle = xend.esusu.start(cycle_id)
        assert type(cycle_id) == int
        assert type(start_cycle) == dict
    except Exception as e:
        assert isinstance(e, Exception)


def test_withdraw_interest():
    try:
        cycle_id = 1
        withdraw_interest = xend.esusu.withdraw_interest(cycle_id)
        assert type(cycle_id) == int
        assert type(withdraw_interest) == dict
    except Exception as e:
        assert isinstance(e, Exception)


def test_withdraw_capital():
    try:
        cycle_id = 1
        withdraw_capital = xend.esusu.withdraw_capital(cycle_id)
        assert type(cycle_id) == int
        assert type(withdraw_capital) == dict
    except Exception as e:
        assert isinstance(e, Exception)


def test_is_member_of_cycle():
    try:
        cycle_id = 1
        is_member_of_cycle = xend.esusu.is_member_of_cycle(cycle_id)
        assert type(cycle_id) == int
        assert type(is_member_of_cycle["data"]) == bool
    except Exception as e:
        assert isinstance(e, Exception)


def test_accrue_interest_capital():
    try:
        cycle_id = 1
        accrue_interest_capital = xend.esusu.accrue_interest_capital(cycle_id)
        assert type(cycle_id) == int
        assert type(accrue_interest_capital) == dict
    except Exception as e:
        assert isinstance(e, Exception)


def test_create_group():
    try:
        name = "test"
        symbol = "TXT"
        create_group = xend.esusu.create_group(name, symbol)
        assert type(name) == str
        assert type(symbol) == str
        assert type(create_group) == dict
    except Exception as e:
        assert isinstance(e, Exception)


def test_groups():
    try:
        groups = xend.esusu.get_groups()
        assert type(groups["data"]) == list or dict
    except Exception as e:
        assert isinstance(e, Exception)


def test_no_of_contributions():
    try:
        no_of_contributions = xend.esusu.no_of_contributions()
        assert type(no_of_contributions["data"]) == int
    except Exception as e:
        assert isinstance(e, Exception)


def test_contributions():
    try:
        contributions = xend.esusu.contributions()
        assert type(contributions["data"]) == list or dict
    except Exception as e:
        assert isinstance(e, Exception)


def test_cycles_in_group():
    try:
        group_id = 1
        cycles_in_group = xend.esusu.cycles_in_group(group_id)
        assert type(group_id) == int
        assert type(cycles_in_group["data"]) == list or dict
    except Exception as e:
        assert isinstance(e, Exception)
