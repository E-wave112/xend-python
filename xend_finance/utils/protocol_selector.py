from typing import List, Union

from xend_finance.models.schemas import Options, Protocols
from xend_finance.environment.testnet import testnet_protocols
from xend_finance.utils.exceptions.handleErrors import BaseError


def get_protocol_essentials(
    protocols: List[Protocols], protocol_name: Union[str, None] = None
):
    """
    It takes a list of protocols and a protocol name,
    and returns a dictionary with the addresses, name, and available protocols

    :param protocols: List[Protocols]
    :type protocols: List[Protocols]
    :param protocol_name: The name of the protocol you want to use.
    If you don't specify one, the first protocol in the list will be used
    :type protocol_name: Union[str, None]
    :return: A dictionary with the following keys:
        - addresses: a list of addresses
        - name: a string
        - available: a list of lists
    """
    if protocol_name:
        # filter the protocols by protocol_name
        requested_protocol = list(
            filter(lambda protocol: protocol["code"] == protocol_name, protocols)
        )
        if len(requested_protocol) > 0:
            protocol_object = requested_protocol[0]
            addresses = protocol_object["addresses"]
            name = protocol_object["name"]
        else:
            protocol_object = protocols[0]
            addresses = protocol_object["addresses"]
            name = protocol_object["name"]
    else:
        protocol_object = protocols[0]
        addresses = protocol_object["addresses"]
        name = protocol_object["name"]
    available = list(map(lambda proto: [proto], protocols))
    return {"addresses": addresses, "name": name, "available": available}


def protocol_selector(options: Options):
    """
    It takes in the options object and returns the protocol essentials
    for the protocol name provided in the options object

    :param options: Options
    :type options: Options
    :return: The protocol essentials are being returned.
    """
    protocol_name = options.protocol_name
    environment = options.env
    local_protocol = options.protocols

    if environment == "testnet":
        return get_protocol_essentials(testnet_protocols, protocol_name)
    elif environment == "local":
        if local_protocol:
            return get_protocol_essentials(local_protocol, protocol_name)
        else:
            raise BaseError({"message": "please provide the protocols to be used"})
    elif environment == "mainnet":
        if local_protocol:
            return get_protocol_essentials(local_protocol, protocol_name)
        else:
            raise BaseError({"message": "failed to initialize mainnet protocols"})
    else:
        raise BaseError({"message": "no environment found"})
