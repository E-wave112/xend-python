from xend_finance.models.schemas import Addresses

# Add
from xend_finance.strategies.contract import getContract
from xend_finance.strategies.abis.index import COOPERATIVE, GROUPS
from xend_finance.utils.exceptions.handleErrors import BaseError
from xend_finance.utils.send_signed_transaction import send_signed_transaction


def create_cooperative_group(
    group_name: str, symbol: str, provider: str, private_key: str, addresses: Addresses
):
    """
    It creates a new cooperative group.

    :param group_name: The name of the cooperative group you want to create
    :type group_name: str
    :param symbol: The symbol of the group
    :type symbol: str
    :param provider: The provider URL
    :type provider: str
    :param private_key: The private key of the user who is creating the group
    :type private_key: str
    :param addresses: Addresses
    :type addresses: Addresses
    :return: A receipt of the transaction
    """
    try:
        group_contract = getContract(provider, GROUPS, addresses.GROUPS)
        contract = getContract(provider, COOPERATIVE, addresses.COOPERATIVE)
        group_exists = group_contract.functions.getGroupIndexerByName(group_name).call()
        if group_exists[0]:
            raise BaseError({"status": "error", "message": "Group already exists"})
        data = contract.functions.createGroup(group_name, symbol).transact()
        receipt = send_signed_transaction(
            private_key, provider, data, contract, addresses.COOPERATIVE, "createGroup"
        )
        return {"status": "success", "data": receipt}
    except BaseError as e:
        raise BaseError({"status": "error", "message": e})
