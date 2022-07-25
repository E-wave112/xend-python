from xend_finance.strategies.contract import getContract
from xend_finance.strategies.abis.index import ABIS
from xend_finance.utils.exceptions.handleErrors import BaseError


def price_per_full_share(provider: str, contract_address: str):
    """
    > Returns the price per full share of the given contract address

    :param provider: The provider you're using to connect to the blockchain
    :type provider: str
    :param contract_address: The address of the contract you want to get the price per full share of
    :type contract_address: str
    :return: The price per full share of the given contract address.
    """
    try:
        contract = getContract(provider, ABIS["PROTOCOL_ADAPTER"], contract_address)
        price_per_full_share = contract.functions.GetPricePerFullShare().call()
        return {"status": "success", "data": price_per_full_share}
    except BaseError as e:
        raise BaseError({"status": "error", "message": e})
