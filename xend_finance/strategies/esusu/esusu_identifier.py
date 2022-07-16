from xend_finance.models.schemas import Addresses
from xend_finance.strategies.contract import getContract
from xend_finance.strategies.abis.index import ESUSU_STORAGE
from xend_finance.utils.exceptions.handleErrors import BaseError
from xend_finance.utils.key_address import private_key_to_address


def get_esusu_id(position: int, provider: str, private_key: str, addresses: Addresses):
    """
    > This function returns the esusu id of the esusu cycle at the specified position
    for the specified client address

    :param position: The position of the esusu cycle in the list of esusu cycles
    created by the client
    :type position: int
    :param provider: The provider you're using to connect to the blockchain
    :type provider: str
    :param private_key: The private key of the user who created the esusu
    :type private_key: str
    :param addresses: This is the address of the contract
    :type addresses: Addresses
    :return: The esusu_id of the esusu cycle at the given position
    """
    try:
        contract = getContract(provider, ESUSU_STORAGE, addresses.ESUSU_STORAGE)
        client_address = private_key_to_address(provider, private_key)
        esusu_id = contract.functions.GetCycleIdFromCycleIndexAndCycleCreator(
            position, client_address
        ).call()
        return {"status": "success", "data": int(esusu_id)}
    except BaseError as e:
        raise BaseError({"status": "error", "message": e})
