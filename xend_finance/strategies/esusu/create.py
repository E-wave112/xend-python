from web3 import Web3

from xend_finance.models.schemas import Addresses, EsusuCycle
from xend_finance.strategies.contract import getContract
from xend_finance.strategies.abis.index import ESUSU_SERVICE
from xend_finance.utils.send_signed_transaction import send_signed_transaction
from xend_finance.utils.exceptions.handleErrors import BaseError


def create_esusu_cycle(args: EsusuCycle, addresses: Addresses):
    """
    It creates an esusu cycle

    :param args: This is the object that contains the parameters passed to the function
    :type args: EsusuCycle
    :param addresses: This is the address of the contract on the blockchain
    :type addresses: Addresses
    :return: A receipt of the transaction
    """
    provider = args.provider
    private_key = args.private_key
    group_id = args.group_id
    deposit_amount = args.deposit_amount
    payout_interval_in_seconds = args.payout_interval_in_seconds
    start_time_in_seconds = args.start_time_in_seconds
    max_members = args.max_members
    try:
        contract = getContract(provider, ESUSU_SERVICE, addresses.ESUSU_SERVICE)
        # convert deposit amount to wei
        deposit_amount_wei = Web3.toWei(deposit_amount, "ether")
        data = contract.functions.CreateEsusu(
            group_id,
            deposit_amount_wei,
            payout_interval_in_seconds,
            start_time_in_seconds,
            max_members,
        ).transact()
        receipt = send_signed_transaction(
            private_key,
            provider,
            data,
            contract,
            addresses.ESUSU_SERVICE,
            "CreateEsusu",
        )
        return {
            "status": "success",
            "message": "Esusu cycle created successfully",
            "data": receipt,
        }
    except BaseError as e:
        raise BaseError(
            {
                "status": "error",
                "message": "Esusu cycle could not be created",
                "data": e,
            }
        )
