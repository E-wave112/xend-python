from xend_finance.models.schemas import Addresses
from xend_finance.strategies.contract import getContract
from xend_finance.strategies.abis.index import COOPERATIVE, GROUPS
from xend_finance.utils.exceptions.handleErrors import BaseError
from xend_finance.utils.send_signed_transaction import send_signed_transaction


def create_cooperative_group(
    group_name: str, symbol: str, provider: str, private_key: str, addresses: Addresses
):
    try:
        group_contract = getContract(provider, GROUPS, addresses.GROUPS)
        contract = getContract(provider, COOPERATIVE, addresses.COOPERATIVE)
        group_exists = group_contract.functions.getGroupIndexerByName(group_name).call()
        print(group_exists)
        if group_exists[0]:
            raise BaseError({"status": "error", "message": "Group already exists"})
        data = contract.functions.createGroup(group_name, symbol).transact()
        receipt = send_signed_transaction(
            private_key, provider, data, contract, addresses.COOPERATIVE, "createGroup"
        )
        return {"status": "success", "data": receipt}
    except BaseError as e:
        raise BaseError({"status": "error", "message": e})
