from typing import Any, List
from web3 import Web3
from web3.middleware import geth_poa_middleware


def getContract(provider: str, abi: List[Any], address: str) -> Web3:
    """Get smart contract instance from web3.
    Args:
        provider (str): Web3 provider.
        abi (List[Any]): Smart contract ABI.
        address (str): Smart contract address.

    Returns:
        Web3: Smart contract instance.
    """
    web3 = Web3(Web3.HTTPProvider(provider))
    # inject the poa compatibility middleware to the web3 instance
    web3.middleware_onion.inject(geth_poa_middleware, layer=0)
    return web3.eth.contract(abi=abi, address=address)
