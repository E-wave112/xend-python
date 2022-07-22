from xend_finance.models.schemas import Options, Addresses, EsusuCycle
from xend_finance.strategies.esusu.contributions import no_of_contributions, esusu_contributions
from xend_finance.strategies.esusu.create import create_esusu_cycle
from xend_finance.strategies.esusu.created_cycles_count import cycles_count, interest_capital
from xend_finance.strategies.esusu.esusu_identifier import get_esusu_id
from xend_finance.strategies.esusu.info import esusu_cycles_in_group, esusu_info
from xend_finance.strategies.esusu.join import join_group
from xend_finance.strategies.esusu.member import check_if_member
from xend_finance.strategies.esusu.start import start_esusu_cycle
from xend_finance.strategies.esusu.withdrawal_capital import withdraw_capital
from xend_finance.strategies.esusu.withdrawal_interest import withdraw_interest
from xend_finance.strategies.group.groups import create_esusu_groups, get_esusu_groups
from xend_finance.utils.exceptions.handleErrors import BaseError


class Esusu:
    """Class that allows users to access esusu related functions"""

    def __init__(
        self, provider: str, private_key: str, options: Options, addresses: Addresses, protocol: str
    ):
        self.provider = provider
        self.private_key = private_key
        self.options = options
        self.addresses = addresses
        self.protocol = protocol

    def create_esusu(self, args: EsusuCycle):
        """
        It creates an esusu cycle

        :param args: This is the data that is passed to the function
        :type args: EsusuCycle
        :return: The return value is a dictionary with the following keys:
            - status: The status of the transaction.
            - message: The message of the transaction.
            - transaction_id: The transaction id of the transaction.
            - transaction_hash: The transaction hash of the transaction.
            - block_hash: The block hash of the transaction.
            - block_
        """
        args = {**args, "private_key": self.private_key, "provider": self.provider}
        args = EsusuCycle(**args)
        # args.private_key = self.private_key
        try:
            return create_esusu_cycle(args, self.addresses)
        except BaseError as e:
            raise BaseError({"status": "error", "message": e})

    def get_cycles_count(self):

        """
        It returns the number of cycles that the user has
        :return: The number of cycles that the user has.
        """
        try:
            return cycles_count(self.provider, self.private_key, self.addresses)
        except BaseError as e:
            raise BaseError({"status": "error", "message": e})

    def get_cycle_id_from_cycles_created(self, position: int):

        """
        It returns the cycle id of the cycle at the specified position in the list of cycles
        created by the
        user

        :param position: The position of the cycle in the list of cycles created by the provider
        :type position: int
        :return: The cycle id is being returned.
        """
        try:
            return get_esusu_id(position, self.provider, self.private_key, self.addresses)
        except BaseError as e:
            raise BaseError({"status": "error", "message": e})

    def get_esusu_info(self, esusu_id: int):
        """
        It returns the information of an esusu group/cycle

        :param esusu_id: The id of the esusu group/cycle
        :type esusu_id: int
        :return: A dictionary with the status and message keys.
        """
        try:
            return esusu_info(esusu_id, self.provider, self.addresses)
        except BaseError as e:
            raise BaseError({"status": "error", "message": e})

    def join(self, cycle_id: int):
        """
        It joins a group.

        :param cycle_id: The cycle id of the cycle you want to join
        :type cycle_id: int
        :return: The return value is a dictionary with the following keys:
            - status: "success" or "error"
            - message: a string with the error message or the transaction hash
            - transaction: the transaction object
            - transaction_receipt: the transaction receipt object
            - contract_address: the contract address
            - contract_instance: the contract instance
        """
        try:
            return join_group(cycle_id, self.provider, self.private_key, self.addresses)
        except BaseError as e:
            raise BaseError({"status": "error", "message": e})

    def start(self, cycle_id: int):
        """
        It starts a cycle by calling the `start_esusu_cycle` function from the `esusu` module

        :param cycle_id: The id of the cycle you want to start
        :type cycle_id: int
        :return: The transaction hash
        """
        try:
            return start_esusu_cycle(cycle_id, self.provider, self.private_key, self.addresses)
        except BaseError as e:
            raise BaseError({"status": "error", "message": e})

    def withdraw_interest(self, esusu_id: int):
        """
        It withdraws interest from the esusu contract

        :param esusu_id: The id of the esusu you want to withdraw interest from
        :type esusu_id: int
        :return: The withdraw_interest function is being returned.
        """
        try:
            return withdraw_interest(esusu_id, self.provider, self.private_key, self.addresses)
        except BaseError as e:
            raise BaseError({"status": "error", "message": e})

    def withdraw_capital(self, cycle_id: int):
        """
        `withdraw_capital(cycle_id, provider, private_key, addresses)`

        This function will withdraw the capital from the cycle with the given cycle_id

        :param cycle_id: The cycle ID of the cycle you want to withdraw capital from
        :type cycle_id: int
        :return: The withdraw_capital function is being returned.
        """
        try:
            return withdraw_capital(cycle_id, self.provider, self.private_key, self.addresses)
        except BaseError as e:
            raise BaseError({"status": "error", "message": e})

    def is_member_of_cycle(self, cycle_id: int):
        """
        `check_if_member(cycle_id, provider, private_key, addresses)`

        This function takes in the cycle_id, the provider, the private_key, and the addresses.
        It then returns a boolean value

        :param cycle_id: The ID of the cycle you want to check
        :type cycle_id: int
        :return: The function is_member_of_cycle() returns a boolean value.
        """
        try:
            return check_if_member(cycle_id, self.private_key, self.provider, self.addresses)
        except BaseError as e:
            raise BaseError({"status": "error", "message": e})

    def accrue_interest_capital(self, cycle_id: int):
        """
        `accrue_interest_capital` is a function that takes in a cycle_id and
        returns the interest capital accrued for that cycle

        :param cycle_id: The cycle number you want to accrue interest for
        :type cycle_id: int
        :return: the amount of interest accrued for the cycle.
        """
        try:
            return interest_capital(cycle_id, self.provider, self.private_key, self.addresses)
        except BaseError as e:
            raise BaseError({"status": "error", "message": e})

    # Create a Group for Esusu cycles
    def create_group(self, name: str, symbol: str):
        """
        It creates a group with the name and symbol provided

        :param name: The name of the group
        :type name: str
        :param symbol: The symbol of the group
        :type symbol: str
        :return: A dictionary with the status and message
        """
        try:
            return create_esusu_groups(
                name, symbol, self.provider, self.private_key, self.addresses
            )
        except BaseError as e:
            raise BaseError({"status": "error", "message": e})

    def get_groups(self):
        """
        It returns a list of groups that the user is a member of
        :return: The get_groups method returns the esusu groups
        """
        try:
            return get_esusu_groups(self.provider, self.private_key, self.addresses)
        except BaseError as e:
            raise BaseError({"status": "error", "message": e})

    def no_of_contributions(self):
        """
        It returns the number of contributions made by the user.
        :return: The number of contributions made by the user.
        """
        try:
            return no_of_contributions(self.provider, self.private_key, self.addresses)
        except BaseError as e:
            raise BaseError({"status": "error", "message": e})

    def contributions(self):
        """
        It returns the contributions of the user to the esusu group
        :return: The contributions of the user.
        """
        try:
            return esusu_contributions(self.provider, self.private_key, self.addresses)
        except BaseError as e:
            raise BaseError({"status": "error", "message": e})

    def cycles_in_group(self, group_id: int):
        """
        It returns a list of all the cycles in a group

        :param group_id: The id of the group you want to get the cycles for
        :type group_id: int
        :return: A list of cycles in a group
        """
        try:
            return esusu_cycles_in_group(group_id, self.provider, self.addresses)
        except BaseError as e:
            raise BaseError({"status": "error", "message": e})
