from pydantic import BaseModel
from typing import List, Any, Optional

# from xend_finance.utils.class_methods import GetSetItems


class Options(BaseModel):
    env: Optional[str]
    protocols: Optional[List[Protocols]]  # noqa: F821
    protocolName: Optional[str]
    layer2: Optional[List[Any]]
    key: Any


class Layer2Addresses(BaseModel):
    name: str
    logo: Optional[str]
    tokenAddress: str
    tokenAbi: List[Any]
    protocolName: str
    protocolAddress: str
    protocolAbi: List[Any]
    network: int
    decimals: int
    widthdrawDecimals: int
    ppfsMethod: str


class Addresses(BaseModel):
    PROTOCOL_ADAPTER: str
    PROTOCOL_SERVICE: str
    GROUPS: str
    CYCLES: str
    ESUSU_SERVICE: str
    ESUSU_STORAGE: str
    ESUSU_ADAPTER: str
    COOPERATIVE: str
    PERSONAL: str
    CLIENT_RECORD: str
    XEND_TOKEN: str
    TOKEN: str
    PROTOCOL_CURRENCY: str


class Protocols(BaseModel):
    name: str
    code: str
    addresses: Addresses


class CooperativeCycleData(BaseModel):
    groupId: int
    cycleStakeAmount: Any
    payoutIntervalInSeconds: int
    startTimeInSeconds: int
    maxMembers: int


class EsusuCycleData(BaseModel):
    groupId: int
    depositAmount: Any
    payoutIntervalInSeconds: int
    startTimeInSeconds: int
    maxMembers: int
