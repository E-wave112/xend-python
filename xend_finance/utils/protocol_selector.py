from typing import List, Union

from xend_finance.models.schemas import Options, Protocols
from xend_finance.environment.testnet import testnet_protocols
from xend_finance.utils.exceptions.handleErrors import BaseError


def get_protocol_essentials(protocols: List[Protocols], protocol_name: Union[str, None] = None):
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
