from xend_finance.models.schemas import Fixed, Options, Addresses
from xend_finance.strategies.individual.fixed_deposit import create_fixed_deposit
from xend_finance.strategies.individual.fixed_withdraw import perform_fixed_withdrawal
from xend_finance.strategies.individual.flexible_deposit import create_flexible_deposit
from xend_finance.strategies.individual.flexible_withdrawal import perform_flexible_withdraw
from xend_finance.strategies.individual.get_fixed_deposit_record import fixed_deposit_record
from xend_finance.strategies.individual.get_flexible_deposit_record import flexible_deposit_record
from xend_finance.utils.exceptions.handleErrors import BaseError


class Personal:
    """
    Class that allows users to access personal related functions
    """

    def __init__(
        self, provider: str, private_key: str, options: Options, address: Addresses, protocol: str
    ):
        """
        `__init__` is a special method that is called when an instance of a class is created

        :param provider: The URL of the Ethereum node you want to connect to
        :type provider: str
        :param private_key: The private key of the account that will be used to sign the transaction
        :type private_key: str
        :param options: This is a dictionary of options that you can pass to the contract
        :type options: Options
        :param address: The address of the contract
        :type address: Addresses
        :param protocol: The protocol to use for the connection
        :type protocol: str
        """
        self.provider = provider
        self.private_key = private_key
        self.options = options
        self.address = address
        self.protocol = protocol

    def flexible_deposit(self, deposit_amount: str):
        """
        It creates a flexible deposit transaction and returns the transaction hash

        :param deposit_amount: The amount of token you want to deposit
        :type deposit_amount: str
        :return: The return value is a dictionary with the following keys:
            - status: "success" or "error"
            - message: the message to be displayed to the user
            - data: the data to be displayed to the user
        """
        try:
            return create_flexible_deposit(
                self.provider, self.private_key, deposit_amount, self.address
            )
        except BaseError as e:
            raise BaseError({"status": "error", "message": e})

    def fixed_deposit(self, deposit_amount: str, lock_period: int):
        """
        It creates a fixed deposit.

        :param deposit_amount: The amount of tokens you want to deposit
        :type deposit_amount: str
        :param lock_period: The number of blocks to lock the deposit for
        :type lock_period: int
        :return: a transaction receipt.
        """
        try:
            args = {
                "private_key": self.private_key,
                "provider": self.provider,
                "deposit_amount": deposit_amount,
                "lock_period": lock_period,
            }
            args = Fixed(**args)
            return create_fixed_deposit(args, self.address)
        except BaseError as e:
            raise BaseError({"status": "error", "message": e})

    def get_fixed_deposit_record(self):
        """
        It returns the fixed deposit record of the address.
        :return: The fixed deposit record is being returned.
        """
        try:
            return fixed_deposit_record(self.provider, self.private_key, self.address)
        except BaseError as e:
            raise BaseError({"status": "error", "message": e})

    def get_flexible_deposit_record(self):
        """
        It returns the flexible deposit record of the user.
        :return: The flexible deposit record is being returned.
        """
        try:
            return flexible_deposit_record(self.provider, self.private_key, self.address)
        except BaseError as e:
            raise BaseError({"status": "error", "message": e})

    def fixed_withdrawal(self, record_id: int):
        """
        `perform_fixed_withdrawal` is a function that takes in a provider, private key, record id,
        and address, and returns a transaction hash

        :param record_id: The ID of the record you want to withdraw from
        :type record_id: int
        :return: The return value is the transaction hash.
        """
        try:
            return perform_fixed_withdrawal(
                self.private_key, self.provider, record_id, self.address
            )
        except BaseError as e:
            raise BaseError({"status": "error", "message": e})

    def flexible_withdrawal(self, amount: str):
        """
        It performs a flexible withdrawal from the smart contract.

        :param amount: The amount of tokens you want to withdraw
        :type amount: str
        :return: The transaction hash is being returned.
        """
        try:
            return perform_flexible_withdraw(
                self.private_key, self.provider, amount, self.address, self.protocol
            )
        except BaseError as e:
            raise BaseError({"status": "error", "message": e})
