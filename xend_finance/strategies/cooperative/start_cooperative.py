from xend_finance.models.schemas import Addresses
from xend_finance.strategies.contract import getContract
from xend_finance.strategies.abis.index import COOPERATIVE
from xend_finance.utils.exceptions.handleErrors import BaseError
from xend_finance.utils.send_signed_transaction import send_signed_transaction


def start_cooperative_cycle(cycle_id: int, provider: str, private_key: str, addresses: Addresses):
    try:
        contract = getContract(provider, COOPERATIVE, addresses.COOPERATIVE)
        data = contract.functions.activateCycle(cycle_id).transact()
        receipt = send_signed_transaction(
            private_key, provider, data, contract, addresses.COOPERATIVE, "activateCycle"
        )
        return {
            "status": "success",
            "message": "Cooperative cycle started successfully",
            "data": receipt,
        }
    except BaseError as e:
        raise BaseError(
            {"status": "error", "message": "Cooperative cycle could not be started", "data": e}
        )
