from xend_finance.models.schemas import Addresses
from xend_finance.strategies.contract import getContract
from xend_finance.strategies.abis.index import ESUSU_STORAGE
from xend_finance.utils.exceptions.handleErrors import BaseError
from xend_finance.utils.key_address import private_key_to_address


def check_if_member(
    cycle_id: int, private_key: str, provider: str, addresses: Addresses
):
    client_address = private_key_to_address(provider, private_key)
    try:
        contract = getContract(provider, ESUSU_STORAGE, addresses.ESUSU_STORAGE)
        is_member = contract.functions.IsMemberInCycle(client_address, cycle_id).call()
        return {"status": "success", "data": bool(is_member)}
    except BaseError as e:
        raise BaseError({"status": "error", "message": e})
