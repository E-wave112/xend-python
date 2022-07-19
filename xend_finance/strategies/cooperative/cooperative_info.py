from xend_finance.models.schemas import Addresses
from xend_finance.strategies.contract import getContract
from xend_finance.strategies.abis.index import CYCLES
from xend_finance.utils.exceptions.handleErrors import BaseError


def get_cooperative_info(cycle_id: int, provider: str, address: Addresses):
    try:
        contract = getContract(provider, CYCLES, address.CYCLES)
        data = contract.functions.getCycleInfoById(cycle_id).call()
        return {"status": "success", "data": data}
    except BaseError as e:
        raise BaseError({"status": "error", "message": e})
