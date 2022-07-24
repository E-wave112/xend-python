from xend_finance.models.schemas import Addresses
from xend_finance.strategies.contract import getContract
from xend_finance.strategies.abis.index import CYCLES
from xend_finance.utils.exceptions.handleErrors import BaseError


def get_cooperative_info(cycle_id: int, provider: str, address: Addresses):
    """
    > This function gets the information of a cooperative cycle by its id

    :param cycle_id: The ID of the cooperative cycle you want to get information about
    :type cycle_id: int
    :param provider: The provider is the URL of the node you want to connect to
    :type provider: str
    :param address: Addresses
    :type address: Addresses
    """
    try:
        contract = getContract(provider, CYCLES, address.CYCLES)
        data = contract.functions.getCycleInfoById(cycle_id).call()
        return {"status": "success", "data": data}
    except BaseError as e:
        raise BaseError({"status": "error", "message": e})
