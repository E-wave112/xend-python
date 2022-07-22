import re
import math
from requests import request
from web3 import Web3

from xend_finance.utils.constants.misc import REGEX_NUMBER_STRING
from xend_finance.utils.constants.provider import PROVIDERS
from xend_finance.utils.constants.chain_id import ChainId


def providers_to_list():
    """
    It takes the values of the PROVIDERS dictionary and turns them into a list.
    :return: A list of the values of the PROVIDERS dictionary.
    """
    providers_list = list(PROVIDERS.values())
    return providers_list


def provider_to_chain_id(provider: str) -> int:
    """
    `provider_to_chain_id` takes a provider URL and returns the chain ID of the
    network it connects to

    :param provider: The URL of the provider you want to use
    :type provider: str
    :return: The chain id of the provider
    """
    providers = providers_to_list()
    provider_val = list(filter(lambda x: x["url"] == provider, providers))
    if len(provider_val) > 0:
        return provider_val[0]["chain"]
    return 0


def check_chain_id(chain_id: int) -> dict:
    """
    > If the chain_id is in the chain_map, return the corresponding provider. Otherwise, return the
    localhost provider

    :param chain_id: The chain ID of the network you want to connect to
    :type chain_id: int
    :return: The provider for the chain_id
    """
    chain_map = {
        ChainId.ETHEREUM_MAINNET.value: PROVIDERS["ETHEREUM_MAINNET"],
        ChainId.BSC_MAINNET.value: PROVIDERS["BSC_MAINNET"],
        ChainId.BSC_TESTNET.value: PROVIDERS["BSC_TESTNET"],
        ChainId.POLYGON_MAINNET.value: PROVIDERS["POLYGON_MAINNET"],
        ChainId.POLYGON_TESTNET.value: PROVIDERS["POLYGON_TESTNET"],
        ChainId.LOCALHOST.value: PROVIDERS["LOCALHOST"],
    }

    return chain_map.get(chain_id, PROVIDERS["LOCALHOST"])


def get_address_by_name(addresses: list, name: str):
    """
    It takes a list of dictionaries and a name, and returns the address of the first
    dictionary in the list whose name matches the name passed in

    :param addresses: list of dictionaries
    :type addresses: list
    :param name: The name of the address you want to filter by
    :type name: str
    :return: The address of the person with the name given.
    """
    address_val = list(filter(lambda x: x["name"] == name, addresses))
    if len(address_val) > 0:
        return address_val[0]["address"]
    return ""


def capitalize_first_letter(string: str) -> str:
    """
    Capitalize the first letter of a string.

    :param string: str - This is the parameter. It's a string
    :type string: str
    :return: The first letter of the string is being capitalized.
    """
    return string.capitalize()


def request_instance(url: str, method: str = "GET", data: dict = {}) -> dict:
    """
    It takes a url, method, and data and returns the response from the request.

    :param url: The url of the request
    :type url: str
    :param method: The method of the request
    :type method: str
    :param data: The data of the request
    :type data: dict
    :return: The response from the request
    """
    response = request(method, url, json=data)
    return response.json()


def parse_float(string) -> float:
    """
    It takes a string, finds all the numbers in it, joins them together, and returns the result as a
    float

    :param string: The string to parse
    :type string: str
    :return: A float
    """
    num_match = re.findall(REGEX_NUMBER_STRING, string)
    num = "".join(num_match)
    return float(num) if num else 0.0


def format_amount(amount, network: int, asset_name: str):
    """
    `format_amount` takes in an amount, a network, and an asset name,
    and returns the amount formatted for the given network and asset

    :param amount: The amount of the asset you want to deposit
    :type amount: Union[int, float,str]
    :param network: The network you're using
    :type network: int
    :param asset_name: The name of the asset you want to get the price of
    :type asset_name: str
    :return: The amount of the asset in the correct format.
    """
    if network == 56:
        return float(Web3.fromWei(amount, "ether"))
    elif network == 137:
        if asset_name == "WBTC":
            return parse_float(str(amount)) * math.pow(10, 8)
        if asset_name == "AAVE":
            return float(Web3.fromWei(amount, "ether"))
        return float(Web3.fromWei(amount, "mwei"))
    else:
        return amount
