import math
from typing import Union
from xend_finance.models.schemas import Addresses
from xend_finance.strategies.abis.index import ABIS
from xend_finance.strategies.contract import getContract
from xend_finance.utils.exceptions.handleErrors import BaseError
from xend_finance.utils.send_signed_transaction import send_signed_transaction


def perform_flexible_withdraw(
    private_key: str,
    provider: str,
    amount: Union[str, float],
    addresses: Addresses,
    protocol: str,
):
    """
    It takes a private key, a provider, an amount, an Addresses object, and a protocol, and returns
    a receipt for a transaction that withdraws the amount from the protocol to the
    address associated with the private key.

    :param private_key: The private key of the account you want to withdraw from
    :type private_key: str
    :param provider: The provider you're using to connect to the blockchain
    :type provider: str
    :param amount: The amount of tokens you want to withdraw
    :type amount: str
    :param addresses: This is an object that contains the addresses of the contracts
    :type addresses: Addresses
    :param protocol: The protocol you want to withdraw from
    :type protocol: str
    :return: A receipt of the transaction
    """
    try:
        if protocol == "Venus":
            amount = float(amount) * math.pow(10, 8)
        amount = float(amount) * math.pow(10, 18)
        contract = getContract(provider, ABIS["PERSONAL"], addresses.PERSONAL)
        data = contract.functions.withdraw(round(amount)).transact()
        receipt = send_signed_transaction(
            private_key, provider, data, contract, addresses.PERSONAL, "withdraw"
        )
        return {"status": "success", "data": receipt}
    except BaseError as e:
        raise BaseError({"status": "error", "message": e})
