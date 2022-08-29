from xend_finance.models.schemas import Addresses
from xend_finance.strategies.contract import getContract
from xend_finance.strategies.abis.index import COOPERATIVE
from xend_finance.utils.exceptions.handleErrors import BaseError
from xend_finance.utils.send_signed_transaction import send_signed_transaction


def perform_ongoing_withdrawal(
    cycle_id: int, provider: str, private_key: str, addresses: Addresses
):
    """It withdraws the funds from the cycle that is currently ongoing

    :param cycle_id: The ID of the cycle you want to withdraw from
    :type cycle_id: int
    :param provider: The provider you're using to connect to the blockchain
    :type provider: str
    :param private_key: The private key of the user who is performing the withdrawal
    :type private_key: str
    :param addresses: Addresses
    :type addresses: Addresses
    :return: a dictionary with the status of the transaction, a message and the data.
    """
    try:
        contract = getContract(provider, COOPERATIVE, addresses.COOPERATIVE)
        data = contract.functions.withdrawFromCycleWhileItIsOngoing(cycle_id).transact()
        receipt = send_signed_transaction(
            private_key,
            provider,
            data,
            contract,
            addresses.COOPERATIVE,
            "withdrawFromCycleWhileItIsOngoing",
        )
        return {
            "status": "success",
            "message": "Withdrawal performed successfully",
            "data": receipt,
        }
    except BaseError as e:
        raise BaseError(
            {"status": "error", "message": "Could not perform withdrawal", "data": e}
        )
