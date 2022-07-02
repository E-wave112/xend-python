from typing import Any, List
from web3 import Web3

def getContract(provider:str, abi:List[Any], address:str) -> Web3:
    """ Get smart contract instance from web3.
    Args:
        provider (str): Web3 provider.
        abi (List[Any]): Smart contract ABI.
        address (str): Smart contract address.

    Returns:
        Web3: Smart contract instance.
    """
    web3 = Web3(Web3.HTTPProvider(provider))
    return web3.eth.contract(abi=abi, address=address)    