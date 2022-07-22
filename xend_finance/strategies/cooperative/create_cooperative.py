from web3 import Web3
from xend_finance.models.schemas import Addresses, CooperativeCycle
from xend_finance.strategies.contract import getContract
from xend_finance.strategies.abis.index import COOPERATIVE
from xend_finance.utils.exceptions.handleErrors import BaseError
from xend_finance.utils.send_signed_transaction import send_signed_transaction


def create_cooperative_cycle(args: CooperativeCycle, addresses: Addresses):
    private_key = args.private_key
    provider = args.provider
    group_id = args.group_id
    cycle_stake_amount = args.cycle_stake_amount
    payout_interval_in_seconds = args.payout_interval_in_seconds
    start_time_in_seconds = args.start_time_in_seconds
    max_members = args.max_members
    try:
        contract = getContract(provider, COOPERATIVE, addresses.COOPERATIVE)
        cycle_stake_amount = Web3.toWei(cycle_stake_amount, "ether")
        data = contract.functions.createCycle(
            group_id,
            start_time_in_seconds,
            payout_interval_in_seconds,
            max_members,
            False,
            cycle_stake_amount,
        ).transact()
        receipt = send_signed_transaction(
            private_key, provider, data, contract, addresses.COOPERATIVE, "createCycle"
        )
        return {
            "status": "success",
            "message": "Cooperative cycle created successfully",
            "data": receipt,
        }
    except BaseError as e:
        raise BaseError({"status": "error", "message": e})
