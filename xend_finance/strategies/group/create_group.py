from xend_finance.models.schemas import Addresses, ArgsCreateGroup
from xend_finance.strategies.abis.index import GROUPS
from xend_finance.strategies.contract import getContract
from xend_finance.utils.exceptions.handleErrors import BaseError
from xend_finance.utils.key_address import private_key_to_address
from xend_finance.utils.send_signed_transaction import send_signed_transaction


def create_group(arg: ArgsCreateGroup, addresses: Addresses):
    """
    This function creates a group on the blockchain

    :param arg: ArgsCreateGroup
    :type arg: ArgsCreateGroup
    :param addresses: This is the address of the contract
    :type addresses: Addresses
    :return: A dictionary with the status and transaction hash
    """
    provider = arg.provider
    group_name = arg.group_name
    private_key = arg.private_key
    group_symbol = arg.group_symbol
    try:
        contract = getContract(provider, GROUPS, addresses.GROUPS)
        client_address = private_key_to_address(provider, private_key)
        data = contract.functions.createGroup(group_name, group_symbol, client_address).transact()
        transaction_hash = send_signed_transaction(
            private_key, provider, data, contract, addresses.GROUPS, "createGroup"
        )
        return {"status": "success", "data": transaction_hash}
    except BaseError as e:
        raise BaseError({"status": "error", "message": e})
