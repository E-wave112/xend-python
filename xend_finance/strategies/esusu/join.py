from xend_finance.models.schemas import Addresses
from xend_finance.strategies.contract import getContract
from xend_finance.strategies.abis.index import ESUSU_SERVICE, TOKEN
from xend_finance.strategies.esusu.info import esusu_info
from xend_finance.utils.exceptions.handleErrors import BaseError
from xend_finance.utils.send_signed_transaction import send_signed_transaction


def join_group(cycle_id: int, provider: str, private_key: str, addresses: Addresses):
    try:
        contract = getContract(provider, ESUSU_SERVICE, addresses.ESUSU_SERVICE)
        token_contract = getContract(provider, TOKEN, addresses.TOKEN)
        # get info about the esusu using the cycle id and the token amount needed to join the group
        esusu_cycle = esusu_info(cycle_id, provider, addresses)
        # approve the transaction
        deposit_amount = esusu_cycle["data"][0]
        approval_data = token_contract.functions.approve(
            addresses.ESUSU_ADAPTER, deposit_amount
        ).transact()
        # sign the transaction
        send_signed_transaction(
            private_key,
            provider,
            approval_data,
            token_contract,
            addresses.TOKEN,
            "approve",
        )
        # execute the join esusu contract function
        data = contract.functions.JoinEsusu(cycle_id).transact()
        receipt = send_signed_transaction(
            private_key, provider, data, contract, addresses.ESUSU_SERVICE, "JoinEsusu"
        )
        return {"status": "success", "data": receipt}
    except BaseError as e:
        raise BaseError({"status": "error", "message": e})
