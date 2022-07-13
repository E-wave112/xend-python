from xend_finance.models.schemas import Addresses, ArgsGetGroup
from xend_finance.strategies.abis.index import ESUSU_ADAPTER
from xend_finance.strategies.contract import getContract
from xend_finance.utils.exceptions.handleErrors import BaseError


def get_group(args: ArgsGetGroup, addresses: Addresses):
    """
    `get_group` returns the group information of a group with a given group id

    :param args: ArgsGetGroup - this is the arguments that will be passed to the function
    :type args: ArgsGetGroup
    :param addresses: This is the address of the contract
    :type addresses: Addresses
    :return: A dictionary with the status and the group information
    """
    provider = args.provider
    group_id = args.group_id
    try:
        contract = getContract(provider, ESUSU_ADAPTER, addresses.ESUSU_ADAPTER)
        data = contract.functions.GetGroupInformationById(group_id).call()
        return {"status": "success", "group": data}
    except BaseError as e:
        raise BaseError({"status": "error", "message": e})
