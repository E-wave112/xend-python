from web3 import Web3

from xend_finance.models.schemas import Addresses
from xend_finance.strategies.abis.index import TOKEN, ABIS
from xend_finance.strategies.contract import getContract
from xend_finance.utils.exceptions.handleErrors import BaseError
from xend_finance.utils.send_signed_transaction import send_signed_transaction


def create_flexible_deposit(
    provider: str, private_key: str, deposit_amount: str, addresses: Addresses
):
    """
    > This function takes in a provider, private key, deposit amount, and addresses object
    and returns a receipt of the transaction

    :param provider: The provider you're using to connect to the blockchain
    :type provider: str
    :param private_key: The private key of the account that will be depositing the funds
    :type private_key: str
    :param deposit_amount: The amount of ether you want to deposit
    :type deposit_amount: str
    :param addresses: Addresses
    :type addresses: Addresses
    :return: The receipt of the transaction
    """
    try:
        contract = getContract(provider, ABIS["PERSONAL"], addresses.PERSONAL)
        token_contract = getContract(provider, TOKEN, addresses.TOKEN)
        # convert deposit_amount to wei
        deposit_amount = Web3.toWei(deposit_amount, "ether")
        # approve the transaction
        personal = addresses.PERSONAL
        approval_data = token_contract.functions.approve(personal, deposit_amount).transact()
        # sign the transaction
        send_signed_transaction(
            private_key, provider, approval_data, token_contract, addresses.TOKEN, "approve"
        )

        data = contract.functions.deposit().transact()
        receipt = send_signed_transaction(
            private_key, provider, data, contract, addresses.PERSONAL, "deposit"
        )
        return {"status": "success", "data": receipt}
    except BaseError as e:
        raise BaseError({"status": "error", "message": e})
