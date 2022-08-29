from xend_finance.models.schemas import Addresses
from xend_finance.strategies.contract import getContract
from xend_finance.strategies.abis.index import COOPERATIVE
from xend_finance.utils.exceptions.handleErrors import BaseError
from xend_finance.utils.send_signed_transaction import send_signed_transaction


def complete_withdrawal(
    cycle_id: int, provider: str, private_key: str, addresses: Addresses
):
    """this method allows a user to complete a withdrawal from a cycle

    :param cycle_id: The ID of the cycle you want to complete the withdrawal for
    :type cycle_id: int
    :param provider: The provider URL
    :type provider: str
    :param private_key: The private key of the account that will be used to sign the transaction
    :type private_key: str
    :param addresses: Addresses
    :type addresses: Addresses
    :return: A dictionary with the status, message, and data.
    """
    try:
        contract = getContract(provider, COOPERATIVE, addresses.COOPERATIVE)
        data = contract.functions.withdrawFromCycle(cycle_id).transact()
        receipt = send_signed_transaction(
            private_key,
            provider,
            data,
            contract,
            addresses.COOPERATIVE,
            "withdrawFromCycle",
        )
        return {
            "status": "success",
            "message": "Withdrawal completed successfully",
            "data": receipt,
        }
    except BaseError as e:
        raise BaseError(
            {"status": "error", "message": "Could not complete withdrawal", "data": e}
        )
