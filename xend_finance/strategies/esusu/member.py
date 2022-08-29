from xend_finance.models.schemas import Addresses
from xend_finance.strategies.contract import getContract
from xend_finance.strategies.abis.index import ESUSU_STORAGE
from xend_finance.utils.exceptions.handleErrors import BaseError
from xend_finance.utils.key_address import private_key_to_address


def check_if_member(
    cycle_id: int, private_key: str, provider: str, addresses: Addresses
):
    """
    It checks if a user is a member of an esusu cycle

    :param cycle_id: The id of the cycle you want to check if the user is a member of
    :type cycle_id: int
    :param private_key: The private key of the user who is checking
    if they are a member of the cycle
    :type private_key: str
    :param provider: The provider you're using to connect to the blockchain
    :type provider: str
    :param addresses: Addresses
    :type addresses: Addresses
    :return: A boolean value indicating if the user is a member of the cycle
    """
    client_address = private_key_to_address(provider, private_key)
    try:
        contract = getContract(provider, ESUSU_STORAGE, addresses.ESUSU_STORAGE)
        is_member = contract.functions.IsMemberInCycle(client_address, cycle_id).call()
        return {"status": "success", "data": bool(is_member)}
    except BaseError as e:
        raise BaseError({"status": "error", "message": e})
