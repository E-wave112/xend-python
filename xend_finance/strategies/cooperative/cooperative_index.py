from xend_finance.models.schemas import Addresses, CooperativeCycle, Options
from xend_finance.strategies.cooperative.cooperative_group import create_cooperative_group
from xend_finance.strategies.cooperative.cooperative_info import get_cooperative_info
from xend_finance.strategies.cooperative.cooperative_member import is_cooperative_member
from xend_finance.strategies.cooperative.cooperatives import contributions, cycles_in_group
from xend_finance.strategies.cooperative.create_cooperative import create_cooperative_cycle
from xend_finance.strategies.cooperative.join_cooperative import join_a_cooperative
from xend_finance.strategies.cooperative.start_cooperative import start_cooperative_cycle
from xend_finance.strategies.cooperative.withdraw_completed import complete_withdrawal
from xend_finance.strategies.cooperative.withdraw_ongoing import perform_ongoing_withdrawal
from xend_finance.strategies.group.groups import get_esusu_groups
from xend_finance.utils.exceptions.handleErrors import BaseError


class Cooperative:
    """
    Class that allows users to access cooperative related functions
    """

    def __init__(
        self, provider: str, private_key: str, options: Options, addresses: Addresses, protocol: str
    ):
        self.private_key = private_key
        self.provider = provider
        self.options = options
        self.addresses = addresses
        self.protocol = protocol

    def create(self, args: CooperativeCycle):

        try:
            args = {**args, "provider": self.provider, "private_key": self.private_key}
            args = CooperativeCycle(**args)
            return create_cooperative_cycle(args, self.addresses)
        except BaseError as e:
            raise BaseError(
                {"status": "error", "message": "Could not create cooperative", "data": e}
            )

    def join(self, cycle_id: int, number_of_stakes: int):

        try:
            return join_a_cooperative(
                cycle_id, number_of_stakes, self.provider, self.private_key, self.addresses
            )
        except BaseError as e:
            raise BaseError({"status": "error", "message": "Could not join cooperative", "data": e})

    def info(self, cycle_id: int):

        try:
            return get_cooperative_info(cycle_id, self.provider, self.addresses)
        except BaseError as e:
            raise BaseError(
                {"status": "error", "message": "Could not get cooperative info", "data": e}
            )

    def cycle_member_exist(self, cycle_id: int):

        try:
            return is_cooperative_member(cycle_id, self.private_key, self.provider, self.addresses)
        except BaseError as e:
            raise BaseError({"status": "error", "message": "Could not check if member", "data": e})

    def start_cycle(self, cycle_id: int):

        try:
            return start_cooperative_cycle(
                cycle_id, self.provider, self.private_key, self.addresses
            )
        except BaseError as e:
            raise BaseError({"status": "error", "message": "Could not start cycle", "data": e})

    def withdraw_from_ongoing_cycle(self, cycle_id: int):

        try:
            return perform_ongoing_withdrawal(
                cycle_id, self.provider, self.private_key, self.addresses
            )
        except BaseError as e:
            raise BaseError(
                {"status": "error", "message": "Could not withdraw from ongoing cycle", "data": e}
            )

    def withdraw_completed(self, cycle_id: int):
        try:
            return complete_withdrawal(cycle_id, self.provider, self.private_key, self.addresses)
        except BaseError as e:
            raise BaseError(
                {"status": "error", "message": "Could not withdraw from completed cycle", "data": e}
            )

    def create_group(self, group_name: str, symbol: str):
        try:
            return create_cooperative_group(
                group_name, symbol, self.provider, self.private_key, self.addresses
            )
        except BaseError as e:
            raise BaseError({"status": "error", "message": "Could not create group", "data": e})

    def get_cooperative_groups(self):
        try:
            return get_esusu_groups(self.provider, self.private_key, self.addresses)
        except BaseError as e:
            raise BaseError({"status": "error", "message": "Could not get groups", "data": e})

    def contributions(self):
        try:
            return contributions(self.provider, self.private_key, self.addresses)
        except BaseError as e:
            raise BaseError(
                {"status": "error", "message": "Could not get contributions", "data": e}
            )

    def cycles_in_group(self, group_id: str):
        try:
            return cycles_in_group(group_id, self.provider, self.addresses)
        except BaseError as e:
            raise BaseError(
                {"status": "error", "message": "Could not get cycles in group", "data": e}
            )
