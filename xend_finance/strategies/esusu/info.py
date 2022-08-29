from xend_finance.models.schemas import Addresses
from xend_finance.strategies.contract import getContract
from xend_finance.strategies.abis.index import ESUSU_SERVICE, ESUSU_STORAGE
from xend_finance.utils.exceptions.handleErrors import BaseError


def esusu_info(esusu_id: int, provider: str, addresses: Addresses):
    """
    It returns the information of an esusu cycle

    :param esusu_id: The id of the esusu cycle you want to get information about
    :type esusu_id: int
    :param provider: The provider of the blockchain network
    :type provider: str
    :param addresses: This is the address of the contract
    :type addresses: Addresses
    :return: The data is being returned as a dictionary.
    """
    try:
        contract = getContract(provider, ESUSU_SERVICE, addresses.ESUSU_SERVICE)
        data = contract.functions.GetEsusuCycle(esusu_id).call()
        return {"status": "success", "data": data}
    except BaseError as e:
        raise BaseError({"status": "error", "message": e})


def esusu_cycles_in_group(group_id: int, provider: str, addresses: Addresses):
    """
    It returns a list of all the cycles in a group

    :param group_id: The id of the group you want to get the cycles in
    :type group_id: int
    :param provider: The provider is the URL of the node you want to connect to
    :type provider: str
    :param addresses: This is the address of the contract
    :type addresses: Addresses
    :return: A list of cycles in a group
    """
    try:
        contract = getContract(provider, ESUSU_STORAGE, addresses.ESUSU_STORAGE)
        cycles_in_group_count = int(
            contract.functions.GetCycleIndexFromGroupId(group_id).call()
        )
        # get cycles in a group
        cycles = []
        if cycles_in_group_count > 0:
            for cycle in range(cycles_in_group_count, 0, -1):
                id_of_esusu_by_position_in_group = (
                    contract.functions.GetCycleIdFromCycleIndexAndGroupId(
                        group_id, cycle
                    ).call()
                )
                data = esusu_info(id_of_esusu_by_position_in_group, provider, addresses)
                cycles.append(data)

        return {"status": "success", "data": cycles}
    except BaseError as e:
        raise BaseError({"status": "error", "message": e})
