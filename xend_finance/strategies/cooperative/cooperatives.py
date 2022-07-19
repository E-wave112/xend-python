from xend_finance.models.schemas import Addresses
from xend_finance.strategies.contract import getContract
from xend_finance.strategies.abis.index import CYCLES
from xend_finance.utils.exceptions.handleErrors import BaseError
from xend_finance.utils.key_address import private_key_to_address


def contributions(provider: str, private_key: str, addresses: Addresses):
    try:
        client_address = private_key_to_address(provider, private_key)
        contract = getContract(provider, CYCLES, addresses.CYCLES)
        count = contract.functions.getRecordIndexLengthForCycleMembersByDepositor(
            client_address
        ).call()
        cycles_list = []
        for index in range(int(count)):
            cycles_index = {}
            cycles_index = contract.functions.getRecordIndexForCycleMembersIndexerByDepositor(
                client_address, index
            ).call()
            # get the cycles info by it's general index
            cycles_info = contract.functions.getCycleMember(str(cycles_index["1"])).call()
            # get the main cycles info by it's id
            cycle = contract.functions.getCycleInfoById(cycles_info["cycleId"]).call()
            cycle_dict = {**cycles_info, **cycle}
            cycles_list.append(cycle_dict)
        return {"status": "success", "data": cycles_list}

    except BaseError as e:
        raise BaseError({"status": "error", "message": e})


def cycles_in_group(group_id: str, provider: str, addresses: Addresses):
    try:
        contract = getContract(provider, CYCLES, addresses.CYCLES)
        count = contract.functions.getRecordIndexLengthForGroupCycleIndexer(group_id).call()
        cycles_list = []
        if int(count) > 0:
            for index in range(int(count)):
                group_exists = contract.functions.getRecordIndexForGroupCycle(
                    group_id, index
                ).call()
                if group_exists[0]:
                    cycles_info = contract.functions.getCycleInfoByIndex(group_exists[1]).call()

                cycles_list.append(cycles_info)
            return {"status": "success", "data": cycles_list}
        else:
            return {"status": "success", "data": []}
    except BaseError as e:
        raise BaseError({"status": "error", "message": e})
