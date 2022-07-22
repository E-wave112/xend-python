from pydantic import BaseModel
from typing import List, Any, Optional


class Options(BaseModel):
    env: Optional[str]
    protocols: Optional[List[Any]]
    protocol_name: Optional[str]
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


class EsusuCycleData(BaseModel):
    group_id: int
    deposit_amount: Any
    payout_interval_in_seconds: int
    start_time_in_seconds: int
    max_members: int


class ArgsCreateGroup(BaseModel):
    private_key: str
    provider: str
    group_name: str
    group_symbol: str


class ArgsGetGroup(BaseModel):
    provider: str
    group_id: int


class Fixed(BaseModel):
    provider: str
    private_key: str
    deposit_amount: Any
    lock_period: int


class EsusuCycle(BaseModel):
    provider: str
    private_key: str
    group_id: int
    deposit_amount: Any
    payout_interval_in_seconds: int
    start_time_in_seconds: int
    max_members: int


class CooperativeCycle(BaseModel):
    provider: str
    private_key: str
    group_id: int
    cycle_stake_amount: Any
    payout_interval_in_seconds: int
    start_time_in_seconds: int
    max_members: int


class CooperativeCycleData(BaseModel):
    group_id: int
    cycle_stake_amount: Any
    payout_interval_in_seconds: int
    start_time_in_seconds: int
    max_members: int
