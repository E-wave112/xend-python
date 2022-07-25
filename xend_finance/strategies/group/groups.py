from xend_finance.models.schemas import Addresses
from xend_finance.strategies.abis.index import GROUPS, ESUSU_SERVICE, ESUSU_ADAPTER
from xend_finance.strategies.contract import getContract
from xend_finance.utils.exceptions.handleErrors import BaseError
from xend_finance.utils.key_address import private_key_to_address
from xend_finance.utils.send_signed_transaction import send_signed_transaction


def create_esusu_groups(
    name: str, symbol: str, provider: str, private_key: str, addresses: Addresses
):
    """
    It creates a new group on the blockchain

    :param name: The name of the group you want to create
    :type name: str
    :param symbol: The symbol of the group you want to create
    :type symbol: str
    :param provider: The provider URL
    :type provider: str
    :param private_key: The private key of the account that will be used to create the group
    :type private_key: str
    :param addresses: Addresses
    :type addresses: Addresses
    :return: A transaction hash
    """
    try:
        groups_contract = getContract(provider, GROUPS, addresses.GROUPS)
        group_exists = groups_contract.functions.getGroupIndexerByName(name).call()
        if group_exists[0]:
            raise BaseError({"status": "error", "message": "Group already exists"})
        new_contract = getContract(provider, ESUSU_SERVICE, addresses.ESUSU_SERVICE)
        data = new_contract.functions.CreateGroup(name, symbol).transact()
        receipt = send_signed_transaction(
            private_key,
            provider,
            data,
            new_contract,
            addresses.ESUSU_SERVICE,
            "CreateGroup",
        )
        return {"status": "success", "data": receipt}
    except BaseError as e:
        raise BaseError({"status": "error", "message": e})


def get_esusu_groups(provider: str, private_key: str, addresses: Addresses):
    """
    It gets all the groups created by a user

    :param provider: The provider you are using to connect to the blockchain
    :type provider: str
    :param private_key: The private key of the user who is trying to get the groups
    :type private_key: str
    :param addresses: Addresses
    :type addresses: Addresses
    :return: A list of esusu groups
    """
    try:
        client_address = private_key_to_address(provider, private_key)

        contract = getContract(provider, GROUPS, addresses.GROUPS)
        esusu_adapter_contract = getContract(
            provider, ESUSU_ADAPTER, addresses.ESUSU_ADAPTER
        )
        groups_count = int(
            contract.functions.getRecordIndexLengthForCreator(client_address).call()
        )
        esusu_groups = []
        for index in range(groups_count, 1, -1):
            group = contract.functions.getGroupForCreatorIndexer(
                client_address, index
            ).call()
            if group["exist"]:
                group_id = group["index"]
                single_group = esusu_adapter_contract.functions.GetGroupInformationById(
                    group_id
                ).call()
                esusu_groups.append(single_group)
        return {"status": "success", "groups": esusu_groups}
    except BaseError as e:
        raise BaseError({"status": "error", "message": e})
