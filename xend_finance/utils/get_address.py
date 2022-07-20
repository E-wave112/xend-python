from typing import List
from xend_finance.models.schemas import Protocols

from xend_finance.utils.helpers import (
    capitalize_first_letter,
    get_address_by_name,
    request_instance,
)
from xend_finance.utils.constants.misc import XEND_BASE_URL
from xend_finance.utils import layer_2_assets


def get_xend_mainnet_addresses():
    """
    It returns the addresses from the Xend Mainnet.
    :return: A list of dictionaries containing the addresses from the Xend Mainnet.
    """
    return request_instance(f"{XEND_BASE_URL}/addresses")["data"]


def get_bsc_mainnet_addresses() -> List[Protocols]:
    protocols: List[Protocols] = []
    data = get_xend_mainnet_addresses()
    if data and type(data) == list:
        for address in data:
            protocol: Protocols = {
                "name": capitalize_first_letter(address["protocol_name"]),
                "code": address["protocol_name"],
                "addresses": {
                    "PROTOCOL_ADAPTER": get_address_by_name(
                        address["addresses"], "protocol_adapter"
                    ),
                    "PROTOCOL_SERVICE": get_address_by_name(
                        address["addresses"], "protocol_service"
                    ),
                    "GROUPS": get_address_by_name(address["addresses"], "groups"),
                    "CYCLES": get_address_by_name(address["addresses"], "cycles"),
                    "ESUSU_SERVICE": get_address_by_name(address["addresses"], "esusu_service"),
                    "ESUSU_STORAGE": get_address_by_name(address["addresses"], "esusu_storage"),
                    "ESUSU_ADAPTER": get_address_by_name(address["addresses"], "esusu_adapter"),
                    "COOPERATIVE": get_address_by_name(address["addresses"], "cooperative"),
                    "PERSONAL": get_address_by_name(address["addresses"], "personal"),
                    "CLIENT_RECORD": get_address_by_name(address["addresses"], "client_record"),
                    "XEND_TOKEN": get_address_by_name(address["addresses"], "xend_token"),
                    "TOKEN": get_address_by_name(address["addresses"], "token"),
                    "PROTOCOL_CURRENCY": get_address_by_name(
                        address["addresses"], "protocol_currency"
                    ),
                },
            }
            protocols.append(protocol)
    return protocols


def get_layer2_protocols():
    return layer_2_assets.layer_assets
