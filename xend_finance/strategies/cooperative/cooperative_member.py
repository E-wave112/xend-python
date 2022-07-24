from xend_finance.models.schemas import Addresses
from xend_finance.strategies.contract import getContract
from xend_finance.strategies.abis.index import CYCLES
from xend_finance.utils.exceptions.handleErrors import BaseError
from xend_finance.utils.key_address import private_key_to_address


def is_cooperative_member(cycle_id: int, private_key: str, provider: str, address: Addresses):
    """
    > This function checks if the client is a member of the cycle

    :param cycle_id: The ID of the cycle you want to check
    :type cycle_id: int
    :param private_key: The private key of the user who is trying to join the cycle
    :type private_key: str
    :param provider: The provider you're using to connect to the blockchain
    :type provider: str
    :param address: Addresses
    :type address: Addresses
    :return: A boolean value.
    """
    try:
        client_address = private_key_to_address(provider, private_key)
        contract = getContract(provider, CYCLES, address.CYCLES)
        member_exist = contract.functions.doesCycleMemberExist(cycle_id, client_address).call()
        return {"status": "success", "data": bool(member_exist)}
    except BaseError as e:
        raise BaseError({"status": "error", "message": e})
