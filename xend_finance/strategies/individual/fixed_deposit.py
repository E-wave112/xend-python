from web3 import Web3

from xend_finance.models.schemas import Addresses, Fixed
from xend_finance.strategies.abis.index import TOKEN, ABIS
from xend_finance.strategies.contract import getContract
from xend_finance.utils.exceptions.handleErrors import BaseError
from xend_finance.utils.send_signed_transaction import send_signed_transaction


def create_fixed_deposit(args: Fixed, addresses: Addresses):
    """
    This function creates a fixed deposit on the blockchain

    :param args: This is the command line arguments that are passed to the function
    :type args: Fixed
    :param addresses: This is the address of the contract on the blockchain
    :type addresses: Addresses
    :return: a dictionary with the status of the transaction and the receipt of the transaction.
    """
    provider = args.provider
    private_key = args.private_key
    deposit_amount = args.deposit_amount
    lock_period = args.lock_period
    try:
        contract = getContract(provider, ABIS["PERSONAL"], addresses.PERSONAL)
        token_contract = getContract(provider, TOKEN, addresses.TOKEN)
        #  convert deposit_amount to wei
        deposit_amount = Web3.toWei(deposit_amount, "ether")
        # approve the transaction
        approval_data = token_contract.functions.approve(
            addresses.PERSONAL, deposit_amount
        ).transact()
        send_signed_transaction(
            private_key, provider, approval_data, token_contract, addresses.TOKEN, "approve"
        )
        data = contract.functions.FixedDeposit(lock_period).transact()
        receipt = send_signed_transaction(
            private_key, provider, data, contract, addresses.PERSONAL, "FixedDeposit"
        )
        return {"status": "success", "data": receipt}
    except BaseError as e:
        raise BaseError({"status": "error", "message": e})
