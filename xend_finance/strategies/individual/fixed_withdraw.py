from xend_finance.models.schemas import Addresses
from xend_finance.strategies.abis.index import ABIS
from xend_finance.strategies.contract import getContract
from xend_finance.utils.exceptions.handleErrors import BaseError
from xend_finance.utils.send_signed_transaction import send_signed_transaction


def perform_fixed_withdrawal(private_key: str, provider: str, record_id: int, addresses: Addresses):
    """
    > This function allows a user to withdraw from a fixed deposit

    :param private_key: The private key of the account that will be used to sign the transaction
    :type private_key: str
    :param provider: The provider you're using to connect to the blockchain
    :type provider: str
    :param record_id: The ID of the record you want to withdraw from
    :type record_id: int
    :param addresses: This is the address of the contract
    :type addresses: Addresses
    :return: A receipt of the transaction
    """
    try:
        contract = getContract(provider, ABIS["PERSONAL"], addresses.PERSONAL)
        data = contract.functions.WithdrawFromFixedDeposit(record_id).transact()
        receipt = send_signed_transaction(
            private_key, provider, data, contract, addresses.PERSONAL, "WithdrawFromFixedDeposit"
        )
        return {"status": "success", "data": receipt}
    except BaseError as e:
        raise BaseError({"status": "error", "message": e})
