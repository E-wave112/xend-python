from xend_finance.models.schemas import Addresses
from xend_finance.strategies.contract import getContract
from xend_finance.strategies.abis.index import CYCLES
from xend_finance.utils.exceptions.handleErrors import BaseError
from xend_finance.utils.key_address import private_key_to_address


def get_cycles_count(provider: str, private_key: str, addresses: Addresses):
    """
    `get_cycles_count` returns the number of cycles that a user has participated in

    :param provider: The URL of the Ethereum node you want to connect to
    :type provider: str
    :param private_key: The private key of the user
    :type private_key: str
    :param addresses: Addresses
    :type addresses: Addresses
    :return: The number of cycles the user is a part of.
    """
    try:
        contract = getContract(provider, CYCLES, addresses.CYCLES)
        client_address = private_key_to_address(provider, private_key)
        cycles_count = (
            contract.functions.getRecordIndexLengthForCycleMembersByDepositor(
                client_address
            ).call()
        )
        return {"status": "success", "data": int(cycles_count)}
    except BaseError as e:
        raise BaseError({"status": "error", "message": e})
