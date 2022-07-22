from web3 import Web3
from web3.middleware import geth_poa_middleware
from xend_finance.utils.helpers import check_chain_id


def initialize_web3(provider: str) -> Web3:
    """Initialize web3 instance.
    Args:
        provider (str): Web3 provider.

    Returns:
        Web3: Web3 instance.
    """
    web3_instance = Web3(Web3.HTTPProvider(provider))
    # inject the poa compatibility middleware to the web3 instance
    web3_instance.middleware_onion.inject(geth_poa_middleware, layer=0)
    return web3_instance


def create_wallet(chain_id: int) -> dict:
    """
    > It creates a new wallet on the specified chain and returns the address and private key of the
    wallet

    :param chain_id: The chain id of the network you want to create a wallet for
    :type chain_id: int
    :return: A dictionary with the address and private key of the wallet
    """

    provider = check_chain_id(chain_id)["url"]
    web3 = initialize_web3(provider)
    wallet = web3.eth.account.create(chain_id)
    # convert the wallet object or byte code to readable format and return it
    return {"address": wallet.address, "private_key": wallet.privateKey.hex()}


def retrieve_wallet(chain_id: int, private_key: str) -> dict:
    """
    > This function takes in a chain_id and a private_key and returns the address
    and private_key of the wallet

    :param chain_id: The chain id of the network you want to retrieve the wallet from
    :type chain_id: int
    :param private_key: The private key of the wallet you want to retrieve
    :type private_key: str
    :return: A dictionary with the address and private key of the wallet.
    """
    provider = check_chain_id(chain_id)["url"]
    web3 = initialize_web3(provider)
    wallet = web3.eth.account.from_key(private_key)
    return {"address": wallet.address, "private_key": wallet.privateKey.hex()}
