from xend_finance.models.schemas import Addresses
from xend_finance.strategies.abis.index import GROUPS
from xend_finance.strategies.contract import getContract
from xend_finance.utils.exceptions.handleErrors import BaseError
from xend_finance.utils.key_address import private_key_to_address


def get_rewards(provider: str, private_key: str, address: Addresses):
    """
    `get_rewards` returns the rewards for a given address

    :param provider: The provider you're using
    :type provider: str
    :param private_key: The private key of the user who is calling the function
    :type private_key: str
    :param address: The address of the contract you want to interact with
    :type address: Addresses
    :return: The amount of Xend tokens that the user has earned from the group.
    """
    client_address = private_key_to_address(provider, private_key)
    try:
        contract = getContract(provider, GROUPS, address.GROUPS)
        data = contract.functions.getXendTokensReward(client_address).call()
        return {"status": "success", "rewards": data}
    except BaseError as e:
        raise BaseError({"status": "error", "message": e})
