from xend_finance.models.schemas import Addresses
from xend_finance.strategies.abis.index import ABIS
from xend_finance.strategies.contract import getContract
from xend_finance.utils.exceptions.handleErrors import BaseError
from xend_finance.utils.key_address import private_key_to_address


def fixed_deposit_record(provider: str, private_key: str, address: Addresses):
    """
    It returns a list of all the fixed deposit records for a particular client

    :param provider: The provider of the blockchain network
    :type provider: str
    :param private_key: The private key of the client
    :type private_key: str
    :param address: Addresses
    :type address: Addresses
    :return: A list of records for a particular client
    """
    try:
        client_address = private_key_to_address(provider, private_key)
        contract = getContract(provider, ABIS["CLIENT_RECORD"], address.CLIENT_RECORD)
        # get the number of records for the client
        individual_deposit_record_count = int(
            contract.functions.GetRecordIndexFromDepositor(client_address).call()
        )
        data = []
        for index in range(individual_deposit_record_count):
            index = index + 1
            # get a particular record id
            record = contract.functions.GetRecordIdFromRecordIndexAndDepositorRecord(
                client_address, index
            ).call()
            # get basic information about the deposit record
            record_info = contract.functions.GetRecordById(record).call()
            data.append(record_info)
        return {"status": "success", "data": data}
    except BaseError as e:
        raise BaseError({"status": "error", "message": e})
