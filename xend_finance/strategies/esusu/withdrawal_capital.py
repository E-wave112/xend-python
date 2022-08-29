from xend_finance.models.schemas import Addresses
from xend_finance.strategies.contract import getContract
from xend_finance.strategies.abis.index import ESUSU_SERVICE
from xend_finance.utils.send_signed_transaction import send_signed_transaction
from xend_finance.utils.exceptions.handleErrors import BaseError


def withdraw_capital(
    cycle_id: int, provider: str, private_key: str, addresses: Addresses
):
    """
    It withdraws the capital from the esusu cycle

    :param cycle_id: The id of the cycle you want to withdraw capital from
    :type cycle_id: int
    :param provider: The provider to use to connect to the blockchain
    :type provider: str
    :param private_key: The private key of the user who is withdrawing the capital
    :type private_key: str
    :param addresses: This is the address of the contract
    :type addresses: Addresses
    :return: A dictionary with the status, message and data.
    """
    try:
        contract = getContract(provider, ESUSU_SERVICE, addresses.ESUSU_SERVICE)
        data = contract.functions.WithdrawCapitalFromEsusuCycle(cycle_id).transact()
        receipt = send_signed_transaction(
            private_key,
            provider,
            data,
            contract,
            addresses.ESUSU_SERVICE,
            "WithdrawCapitalFromEsusuCycle",
        )
        return {
            "status": "success",
            "message": "Capital withdrawn successfully",
            "data": receipt,
        }
    except BaseError as e:
        raise BaseError(
            {"status": "error", "message": "Capital could not be withdrawn", "data": e}
        )
