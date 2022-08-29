from xend_finance.models.schemas import Addresses
from xend_finance.strategies.contract import getContract
from xend_finance.strategies.abis.index import ESUSU_SERVICE
from xend_finance.utils.send_signed_transaction import send_signed_transaction
from xend_finance.utils.exceptions.handleErrors import BaseError


def withdraw_interest(
    esusu_id: int, provider: str, private_key: str, addresses: Addresses
):
    """
    It withdraws the interest earned by the user from the esusu cycle

    :param esusu_id: The id of the esusu cycle you want to withdraw interest from
    :type esusu_id: int
    :param provider: The provider to use to connect to the blockchain
    :type provider: str
    :param private_key: The private key of the user who is withdrawing the interest
    :type private_key: str
    :param addresses: This is the address of the contract
    :type addresses: Addresses
    :return: A dictionary with the status, message and data.
    """
    try:
        contract = getContract(provider, ESUSU_SERVICE, addresses.ESUSU_SERVICE)
        data = contract.functions.WithdrawROIFromEsusuCycle(esusu_id).transact()
        receipt = send_signed_transaction(
            private_key,
            provider,
            data,
            contract,
            addresses.ESUSU_SERVICE,
            "WithdrawROIFromEsusuCycle",
        )
        return {
            "status": "success",
            "message": "Interest withdrawn successfully",
            "data": receipt,
        }
    except BaseError as e:
        raise BaseError(
            {"status": "error", "message": "Interest could not be withdrawn", "data": e}
        )
