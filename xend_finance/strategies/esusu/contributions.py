from xend_finance.models.schemas import Addresses
from xend_finance.strategies.contract import getContract
from xend_finance.strategies.abis.index import ESUSU_STORAGE
from xend_finance.strategies.esusu.info import esusu_info
from xend_finance.utils.exceptions.handleErrors import BaseError
from xend_finance.utils.key_address import private_key_to_address


def no_of_contributions(provider: str, private_key: str, addresses: Addresses):
    """
    `no_of_contributions` returns the number of contributions made by the member

    :param provider: The provider you're using to connect to the blockchain
    :type provider: str
    :param private_key: The private key of the user
    :type private_key: str
    :param addresses: This is the address of the contract
    :type addresses: Addresses
    :return: The number of contributions made by the client
    """
    try:
        contract = getContract(provider, ESUSU_STORAGE, addresses.ESUSU_STORAGE)
        client_address = private_key_to_address(provider, private_key)
        contributions = contract.functions.GetCycleIndexFromCycleMember(
            client_address
        ).call()
        return {"status": "success", "data": int(contributions)}
    except BaseError as e:
        raise BaseError({"status": "error", "message": e})


def esusu_contributions(provider: str, private_key: str, addresses: Addresses):
    """
    It returns a list of all the esusu cycles that a user has contributed to

    :param provider: The provider of the blockchain network
    :type provider: str
    :param private_key: The private key of the user
    :type private_key: str
    :param addresses: This is the addresses object that contains the addresses of the
    smart contracts
    :type addresses: Addresses
    :return: A list of dictionaries containing the roi balance, capital, and
    cycle of the contribution.
    """
    try:
        contract = getContract(provider, ESUSU_STORAGE, addresses.ESUSU_STORAGE)
        client_address = private_key_to_address(provider, private_key)
        esusu_contributed_list = contract.functions.GetCycleIndexFromCycleMember(
            client_address
        ).call()
        contributions = int(esusu_contributed_list)
        contributions_list = []
        for cycle in range(1, contributions):
            contribution_cycle_id = (
                contract.functions.GetCycleIdFromCycleIndexAndCycleMember(
                    cycle, client_address
                ).call()
            )
            contribution_cycle = esusu_info(contribution_cycle_id, provider, addresses)
            # get the roi balance of the contribution cycle
            roi_balance = contract.functions.GetMemberCycleToBeneficiaryMapping(
                contribution_cycle_id, client_address
            ).call()
            capital = contract.functions.GetMemberWithdrawnCapitalInEsusuCycle(
                contribution_cycle_id, client_address
            ).call()
            # esusu_contributed = esusu_info(provider, private_key, addresses, esusu_id)
            contributions_list.append(
                {
                    "roi_balance": roi_balance,
                    "capital": capital,
                    "cycle": contribution_cycle,
                }
            )
        return {"status": "success", "data": contributions_list}
    except BaseError as e:
        raise BaseError({"status": "error", "message": e})
