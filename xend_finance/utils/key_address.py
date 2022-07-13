# from web3 import Web3  # noqa: F401
from xend_finance.utils.web3_utils import initialize_web3


def private_key_to_address(provider: str, private_key: str) -> str:
    """Convert private key to a wallet address.
    Args:
        privateKey (str): Private key.

    Returns:
        str: Address.
    """
    web3 = initialize_web3(provider)
    wallet = web3.eth.account.from_key(private_key)
    return wallet.address


# print(privateKeyToAddress("http://localhost:8545",
# "0xdc2c0383fdb2515d5a34b43c92c267bd8e55a04113ba4f296d8c20924f6defcf"))
