from xend_finance.models.schemas import Addresses
from xend_finance.strategies.contract import getContract
from xend_finance.strategies.abis.index import ESUSU_STORAGE
from xend_finance.utils.exceptions.handleErrors import BaseError
from xend_finance.utils.key_address import private_key_to_address


def cycles_count(provider: str, private_key: str, addresses: Addresses):
    """
    > This function returns the number of cycles a client has created

    :param provider: The provider you're using to connect to the blockchain
    :type provider: str
    :param private_key: The private key of the user who wants to get the number of cycles they have
    created
    :type private_key: str
    :param addresses: This is the address of the contract
    :type addresses: Addresses
    :return: The number of cycles the client has created
    """
    try:
        contract = getContract(provider, ESUSU_STORAGE, addresses.ESUSU_STORAGE)
        client_address = private_key_to_address(provider, private_key)
        cycles_count = contract.functions.GetCycleIndexFromCycleCreator(client_address).call()
        return {"status": "success", "data": int(cycles_count)}
    except BaseError as e:
        raise BaseError({"status": "error", "message": e})


def interest_capital(cycle_id: int, provider: str, private_key: str, addresses: Addresses):
    """
    `interest_capital` returns the capital and interest of a member in a cycle

    :param cycle_id: The cycle id of the cycle you want to get the capital and interest for
    :type cycle_id: int
    :param provider: The provider of the blockchain
    :type provider: str
    :param private_key: The private key of the user who is trying to withdraw
    :type private_key: str
    :param addresses: This is the address of the contract
    :type addresses: Addresses
    :return: The capital and interest of a member in a cycle
    """
    try:
        contract = getContract(provider, ESUSU_STORAGE, addresses.ESUSU_STORAGE)
        client_address = private_key_to_address(provider, private_key)
        capital = contract.functions.GetMemberWithdrawnCapitalInEsusuCycle(
            cycle_id, client_address
        ).call()
        interest = contract.functions.GetMemberCycleToBeneficiaryMapping(
            cycle_id, client_address
        ).call()
        return {"status": "success", "data": {"capital": capital, "interest": interest}}
    except BaseError as e:
        raise BaseError({"status": "error", "message": e})
