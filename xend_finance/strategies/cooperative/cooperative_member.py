from xend_finance.models.schemas import Addresses
from xend_finance.strategies.contract import getContract
from xend_finance.strategies.abis.index import CYCLES
from xend_finance.utils.exceptions.handleErrors import BaseError
from xend_finance.utils.key_address import private_key_to_address


def is_cooperative_member(cycle_id: int, private_key: str, provider: str, address: Addresses):
    try:
        client_address = private_key_to_address(provider, private_key)
        contract = getContract(provider, CYCLES, address.CYCLES)
        member_exist = contract.functions.doesCycleMemberExist(cycle_id, client_address).call()
        return {"status": "success", "data": bool(member_exist)}
    except BaseError as e:
        raise BaseError({"status": "error", "message": e})
