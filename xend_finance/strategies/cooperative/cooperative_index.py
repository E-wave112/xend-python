from typing import Dict, Union
from xend_finance.models.schemas import Addresses, CooperativeCycle, Options
from xend_finance.strategies.cooperative.cooperative_group import (
    create_cooperative_group,
)
from xend_finance.strategies.cooperative.cooperative_info import get_cooperative_info
from xend_finance.strategies.cooperative.cooperative_member import is_cooperative_member
from xend_finance.strategies.cooperative.cooperatives import (
    contributions,
    cycles_in_group,
)
from xend_finance.strategies.cooperative.create_cooperative import (
    create_cooperative_cycle,
)
from xend_finance.strategies.cooperative.join_cooperative import join_a_cooperative
from xend_finance.strategies.cooperative.start_cooperative import (
    start_cooperative_cycle,
)
from xend_finance.strategies.cooperative.withdraw_completed import complete_withdrawal
from xend_finance.strategies.cooperative.withdraw_ongoing import (
    perform_ongoing_withdrawal,
)
from xend_finance.strategies.group.groups import get_esusu_groups
from xend_finance.utils.exceptions.handleErrors import BaseError


class Cooperative:
    """
    Class that allows users to access cooperative related functions
    """

    def __init__(
        self,
        provider: str,
        private_key: str,
        options: Options,
        addresses: Addresses,
        protocol: str,
    ):
        self.private_key = private_key
        self.provider = provider
        self.options = options
        self.addresses = addresses
        self.protocol = protocol

    def create(self, args: Union[CooperativeCycle, Dict[str, str]]):
        """
        This method creates a cooperative cycle
        It takes a CooperativeCycle object, and returns a transaction hash

        :param args: CooperativeCycle
        :type args: CooperativeCycle
        :return: A CooperativeCycle object
        """

        try:
            args = {**args, "provider": self.provider, "private_key": self.private_key}
            args = CooperativeCycle(**args)
            return create_cooperative_cycle(args, self.addresses)
        except BaseError as e:
            raise BaseError(
                {
                    "status": "error",
                    "message": "Could not create cooperative",
                    "data": e,
                }
            )

    def join(self, cycle_id: int, number_of_stakes: int):
        """
        This method allows a user to join a cooperative cycle
        `join_a_cooperative` is a function that takes in a cycle_id, number_of_stakes, provider,
        private_key, and addresses and returns a transaction hash

        :param cycle_id: The id of the cycle you want to join
        :type cycle_id: int
        :param number_of_stakes: The number of stakes you want to join the cooperative with
        :type number_of_stakes: int
        :return: The join cycle object
        """

        try:
            return join_a_cooperative(
                cycle_id,
                number_of_stakes,
                self.provider,
                self.private_key,
                self.addresses,
            )
        except BaseError as e:
            raise BaseError(
                {"status": "error", "message": "Could not join cooperative", "data": e}
            )

    def info(self, cycle_id: int):
        """
        It returns the cooperative info of a cycle

        :param cycle_id: The cycle id of the cooperative you want to get info about
        :type cycle_id: int
        :return: The cooperative info
        """

        try:
            return get_cooperative_info(cycle_id, self.provider, self.addresses)
        except BaseError as e:
            raise BaseError(
                {
                    "status": "error",
                    "message": "Could not get cooperative info",
                    "data": e,
                }
            )

    def cycle_member_exist(self, cycle_id: int):
        """
        It checks if the user is a cooperative member

        :param cycle_id: The cycle id of the cycle you want to check if you are a member of
        :type cycle_id: int
        :return: The function is_cooperative_member() returns a boolean value.
        """

        try:
            return is_cooperative_member(
                cycle_id, self.private_key, self.provider, self.addresses
            )
        except BaseError as e:
            raise BaseError(
                {"status": "error", "message": "Could not check if member", "data": e}
            )

    def start_cycle(self, cycle_id: int):
        """
        This method starts a cooperative cycle
        `start_cycle` is a function that takes in a cycle_id and returns a transaction hash

        :param cycle_id: The id of the cycle you want to start
        :type cycle_id: int
        :return: The start_cycle function returns a transaction hash.
        """

        try:
            return start_cooperative_cycle(
                cycle_id, self.provider, self.private_key, self.addresses
            )
        except BaseError as e:
            raise BaseError(
                {"status": "error", "message": "Could not start cycle", "data": e}
            )

    def withdraw_from_ongoing_cycle(self, cycle_id: int):
        """
        It takes a cycle ID, and then it performs a withdrawal from that ongoing cycle

        :param cycle_id: The ID of the cycle you want to withdraw from
        :type cycle_id: int
        :return: The return value is a dictionary with the following keys:
            - status: "success" or "error"
            - message: A message describing the result of the operation
            - data: The data returned by the operation
        """

        try:
            return perform_ongoing_withdrawal(
                cycle_id, self.provider, self.private_key, self.addresses
            )
        except BaseError as e:
            raise BaseError(
                {
                    "status": "error",
                    "message": "Could not withdraw from ongoing cycle",
                    "data": e,
                }
            )

    def withdraw_completed(self, cycle_id: int):
        """
        This method allows a user perform withdrawl from a completed cooperative cycle
        `complete_withdrawal` is a function that takes in a cycle id, a provider, a private key,
        and a list of addresses, and returns a transaction hash

        :param cycle_id: The ID of the cycle you want to withdraw from
        :type cycle_id: int
        :return: The withdraw_completed function is being returned.
        """
        try:
            return complete_withdrawal(
                cycle_id, self.provider, self.private_key, self.addresses
            )
        except BaseError as e:
            raise BaseError(
                {
                    "status": "error",
                    "message": "Could not withdraw from completed cycle",
                    "data": e,
                }
            )

    def create_group(self, group_name: str, symbol: str):
        """
        `create_group` creates a new cooperative group

        :param group_name: The name of the group you want to create
        :type group_name: str
        :param symbol: The symbol of the group you want to create
        :type symbol: str
        :return: The group address is being returned.
        """
        try:
            return create_cooperative_group(
                group_name, symbol, self.provider, self.private_key, self.addresses
            )
        except BaseError as e:
            raise BaseError(
                {"status": "error", "message": "Could not create group", "data": e}
            )

    def get_cooperative_groups(self):
        """
        It gets the cooperative groups of the user
        :return: The get_cooperative_groups function returns a list of cooperative groups.
        """
        try:
            return get_esusu_groups(self.provider, self.private_key, self.addresses)
        except BaseError as e:
            raise BaseError(
                {"status": "error", "message": "Could not get groups", "data": e}
            )

    def contributions(self):
        """
        It returns the contributions of the user.
        :return: The contributions of the addresses.
        """
        try:
            return contributions(self.provider, self.private_key, self.addresses)
        except BaseError as e:
            raise BaseError(
                {"status": "error", "message": "Could not get contributions", "data": e}
            )

    def cycles_in_group(self, group_id: str):
        """
        It returns the cycles in a cooperative group.

        :param group_id: The id of the cooperative group you want to get the cycles for
        :type group_id: str
        :return: A list of cycles in a cooperative group
        """
        try:
            return cycles_in_group(group_id, self.provider, self.addresses)
        except BaseError as e:
            raise BaseError(
                {
                    "status": "error",
                    "message": "Could not get cycles in group",
                    "data": e,
                }
            )
