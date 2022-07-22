from xend_finance.models.schemas import Addresses
from xend_finance.strategies.contract import getContract
from xend_finance.strategies.abis.index import ESUSU_SERVICE
from xend_finance.utils.send_signed_transaction import send_signed_transaction
from xend_finance.utils.exceptions.handleErrors import BaseError


def start_esusu_cycle(cycle_id: int, provider: str, private_key: str, addresses: Addresses):
    try:
        contract = getContract(provider, ESUSU_SERVICE, addresses.ESUSU_SERVICE)
        data = contract.functions.StartEsusuCycle(cycle_id).transact()
        receipt = send_signed_transaction(
            private_key, provider, data, contract, addresses.ESUSU_SERVICE, "StartEsusuCycle"
        )
        return {"status": "success", "message": "Esusu cycle started successfully", "data": receipt}
    except BaseError as e:
        raise BaseError(
            {"status": "error", "message": "Esusu cycle could not be started", "data": e}
        )
