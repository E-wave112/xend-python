from xend_finance.models.schemas import Addresses
from xend_finance.strategies.abis.index import ABIS
from xend_finance.strategies.contract import getContract
from xend_finance.utils.exceptions.handleErrors import BaseError
from xend_finance.utils.key_address import private_key_to_address


def flexible_deposit_record(provider: str, private_key: str, address: Addresses):
    """
    This function takes in a provider, private key, and address object and returns the balance of
    the client's deposit record

    :param provider: The provider you're using to connect to the blockchain
    :type provider: str
    :param private_key: The private key of the user's wallet
    :type private_key: str
    :param address: Addresses
    :type address: Addresses
    :return: The balance of the client's account.
    """
    try:
        client_address = private_key_to_address(provider, private_key)
        contract = getContract(provider, ABIS["CLIENT_RECORD"], address.CLIENT_RECORD)
        # get the number of records for the client
        record_count = contract.functions.getClientRecordByAddress(client_address).call()
        share_balance = record_count["derivativeBalance"]
        lending_balance_contract = getContract(
            provider, ABIS["PROTOCOL_ADAPTER"], address.PROTOCOL_ADAPTER
        )
        price_per_full_share = lending_balance_contract.functions.GetPricePerFullShare().call()
        balance = float(price_per_full_share) * float(share_balance) / 10**18
        if record_count:
            return {
                "status": "success",
                "balance": balance,
                "derivativeWithdrawn": record_count["derivativeWithdrawn"],
                "shareBalance": share_balance,
            }
        else:
            return {
                "status": "success",
                "balance": balance,
                "derivativeWithdrawn": 0.0,
                "shareBalance": 0.0,
            }
    except BaseError as e:
        raise BaseError({"status": "error", "message": e})
