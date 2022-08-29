from xend_finance.models.schemas import Addresses
from xend_finance.strategies.contract import getContract
from xend_finance.strategies.abis.index import ESUSU_SERVICE, TOKEN
from xend_finance.strategies.esusu.info import esusu_info
from xend_finance.utils.exceptions.handleErrors import BaseError
from xend_finance.utils.send_signed_transaction import send_signed_transaction


def join_group(cycle_id: int, provider: str, private_key: str, addresses: Addresses):
    """
    It approves the transaction to join the esusu group and then executes the `JoinEsusu` contract
    function

    :param cycle_id: the id of the esusu cycle you want to join
    :type cycle_id: int
    :param provider: The provider is the url of the blockchain node you are connecting to
    :type provider: str
    :param private_key: The private key of the user who is joining the group
    :type private_key: str
    :param addresses: This is the address of the contract
    :type addresses: Addresses
    :return: The receipt of the transaction
    """
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
