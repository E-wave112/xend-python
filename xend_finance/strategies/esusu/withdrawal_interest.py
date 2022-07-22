from xend_finance.models.schemas import Addresses
from xend_finance.strategies.contract import getContract
from xend_finance.strategies.abis.index import ESUSU_SERVICE
from xend_finance.utils.send_signed_transaction import send_signed_transaction
from xend_finance.utils.exceptions.handleErrors import BaseError


def withdraw_interest(esusu_id: int, provider: str, private_key: str, addresses: Addresses):
    try:
        contract = getContract(provider, ESUSU_SERVICE, addresses.ESUSU_SERVICE)
        data = contract.functions.WithdrawROIFromEsusuCycle(esusu_id).transact()
        receipt = send_signed_transaction(
            private_key,
            provider,
            data,
            contract,
            addresses.ESUSU_SERVICE,
            "WithdrawROIFromEsusuCycle",
        )
        return {"status": "success", "message": "Interest withdrawn successfully", "data": receipt}
    except BaseError as e:
        raise BaseError(
            {"status": "error", "message": "Interest could not be withdrawn", "data": e}
        )
