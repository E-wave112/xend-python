from web3 import Web3
from xend_finance.models.schemas import Addresses
from xend_finance.strategies.abis.index import ABIS
from xend_finance.strategies.contract import getContract
from xend_finance.utils.exceptions.handleErrors import BaseError
from xend_finance.utils.key_address import private_key_to_address


def get_balance(provider: str, private_key: str, address: Addresses):
    """
    > This function takes a provider, private key, and address object and returns the balance of the
    address associated with the private key

    :param provider: The provider you're using
    :type provider: str
    :param private_key: The private key of the account you want to get the balance of
    :type private_key: str
    :param address: Addresses
    :type address: Addresses
    :return: A dictionary with the status and balance of the user.
    """
    try:
        client_address = private_key_to_address(provider, private_key)
        contract = getContract(provider, ABIS["TOKEN"], address.TOKEN)
        balance = contract.functions.balanceOf(client_address).call()
        # convert balance to ether
        balance = Web3.fromWei(balance, "ether")
        return {"status": "success", "balance": float(balance)}
    except BaseError as e:
        raise BaseError({"status": "error", "message": e})
