from xend_finance.models.schemas import Addresses, ArgsCreateGroup, ArgsGetGroup
from xend_finance.strategies.group.create_group import create_group
from xend_finance.strategies.group.get_group import get_group
from xend_finance.strategies.group.get_reward import get_rewards
from xend_finance.strategies.group.groups import get_esusu_groups
from xend_finance.utils.exceptions.handleErrors import BaseError


class Group:

    """Class that allows users to access group related functions"""

    def __init__(self, provider: str, private_key: str, addresses: Addresses):
        """
        This function initializes the class with the provider, private key, and addresses

        :param provider: The URL of the Ethereum node you want to connect to
        :type provider: str
        :param private_key: The private key of the account you want to use to sign the transaction
        :type private_key: str
        :param addresses: This is a list of addresses that you want to monitor
        :type addresses: Addresses
        """
        self.provider = provider
        self.private_key = private_key
        self.addresses = addresses

    def create(self, name: str, symbol: str):
        """
        It creates a group.

        :param name: The name of the group you want to create
        :type name: str
        :param symbol: The symbol of the group you want to create
        :type symbol: str
        :return: The group address
        """
        try:
            create_group_args: ArgsCreateGroup = {
                "private_key": self.private_key,
                "provider": self.provider,
                "group_name": name,
                "group_symbol": symbol,
            }
            create_group_args = ArgsCreateGroup(**create_group_args)
            return create_group(create_group_args, self.addresses)
        except BaseError as e:
            raise BaseError({"status": "error", "message": e})

    def get_single_group(self, group_id: int):
        """
        It gets a single group from the database.

        :param group_id: The id of the group you want to get
        :type group_id: int
        :return: A list of groups
        """
        try:
            get_group_args: ArgsGetGroup = {
                "provider": self.provider,
                "group_id": group_id,
            }
            get_group_args = ArgsGetGroup(**get_group_args)
            return get_group(get_group_args, self.addresses)
        except BaseError as e:
            raise BaseError({"status": "error", "message": e})

    def get_groups(self):
        """
        It returns a list of groups that the user is a member of
        :return: A list of groups
        """
        try:
            return get_esusu_groups(self.provider, self.private_key, self.addresses)
        except BaseError as e:
            raise BaseError({"status": "error", "message": e})

    def get_xend_rewards(self):
        """
        It returns the rewards for the addresses in the `addresses` array
        :return: The rewards are being returned.
        """
        try:
            return get_rewards(self.provider, self.private_key, self.addresses)
        except BaseError as e:
            raise BaseError({"status": "error", "message": e})
