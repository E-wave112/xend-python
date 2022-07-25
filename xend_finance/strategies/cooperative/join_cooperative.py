from xend_finance.models.schemas import Addresses
from xend_finance.strategies.contract import getContract
from xend_finance.strategies.abis.index import COOPERATIVE, TOKEN
from xend_finance.strategies.cooperative.cooperative_info import get_cooperative_info
from xend_finance.utils.exceptions.handleErrors import BaseError
from xend_finance.utils.send_signed_transaction import send_signed_transaction


def join_a_cooperative(
    cycle_id: int,
    number_of_stakes: int,
    provider: str,
    private_key: str,
    addresses: Addresses,
):
    try:
        contract = getContract(provider, COOPERATIVE, addresses.COOPERATIVE)
        token_contract = getContract(provider, TOKEN, addresses.TOKEN)

        # get the cooperative with the cycleID passed to this function.
        # this is important because the cooperative cycle amount is needed
        # to approve the transaction
        cooperative_cycle_info = get_cooperative_info(cycle_id, provider, addresses)
        # get the cycle stake amount
        cycle_stake_amount = cooperative_cycle_info["data"][0]
        deposit_amount = cycle_stake_amount * number_of_stakes
        # approve the smart contract to spend the deposit amount
        approval_data = token_contract.functions.approve(
            addresses.COOPERATIVE, deposit_amount
        ).transact()
        send_signed_transaction(
            private_key,
            provider,
            approval_data,
            token_contract,
            addresses.TOKEN,
            "approve",
        )

        # initiate the join cooperative smart contract transaction
        data = contract.functions.joinCycle(cycle_id, number_of_stakes).transact()
        receipt = send_signed_transaction(
            private_key, provider, data, contract, addresses.COOPERATIVE, "joinCycle"
        )
        return {"status": "success", "data": receipt}
    except BaseError as e:
        raise BaseError(
            {"status": "error", "message": "Could not join cooperative", "data": e}
        )
