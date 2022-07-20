from xend_finance.strategies.abis.file_handler import read_abis

GROUPS = read_abis("./Groups.json")
ESUSU_SERVICE = read_abis("./EsusuService.json")
ESUSU_ADAPTER = read_abis("./EsusuAdapter.json")
ESUSU_STORAGE = read_abis("./EsusuStorage.json")
COOPERATIVE = read_abis("./XendFinanceGroup.json")
FADAPTER = read_abis("./FortubeAdapterTestnet.json")
TOKEN = read_abis("./DaiContract.json")
PERSONAL = read_abis("./XendFinanceIndividual_Yearn_V1.json")
CLIENT_RECORD = read_abis("./ClientRecord.json")
CYCLES = read_abis("./Cycles.json")
PROTOCOL_ADAPTER = read_abis("./ProtocolAdapter.json")
XAUTO = read_abis("./xAuto.json")
XVAULT = read_abis("./xVault.json")
ERC20 = read_abis("./ER20.json")
BUSD = read_abis("./busd.json")

# v2 XVault BSC
xvVaultUSDCV2 = read_abis("./V2XVault/XVaultUSDCV2.json")
xvVaultUSDTV2 = read_abis("./V2XVault/XVaultUSDTV2.json")
xvVaultBUSDV2 = read_abis("./V2XVault/XVaultBUSDV2.json")

# v2 XAuto BSC
xvAutoBSCBUSDV2 = read_abis("./V2XAuto/xvAutoBUSDV2.json")
xvAutoBSCUSDCV2 = read_abis("./V2XAuto/xvAutoUSDCV2.json")
xvAutoBSCUSDTV2 = read_abis("./V2XAuto/xvAutoUSDTV2.json")
xvAutoBSCBNBV2 = read_abis("./V2XAuto/xvAutoBNBV2.json")

# //v2 XAuto Matic
xvAutoUSDCV2Matic = read_abis("./V2XAutoMatic/xvAutoUSDCV2.json")
xvAutoUSDTV2Matic = read_abis("./V2XAutoMatic/xvAutoUSDTV2.json")
xvAutoAAVEV2Matic = read_abis("./V2XAutoMatic/xvAutoAAVEV2.json")
xvAutoWBTCV2Matic = read_abis("./V2XAutoMatic/xvAutoWBTCV2.json")

# create a key value pair for the abis

ABIS = {
    "BUSD": BUSD,
    "GROUPS": GROUPS,
    "ESUSU_SERVICE": ESUSU_SERVICE,
    "ESUSU_ADAPTER": ESUSU_ADAPTER,
    "ESUSU_STORAGE": ESUSU_STORAGE,
    "COOPERATIVE": COOPERATIVE,
    "TOKEN": TOKEN,
    "PERSONAL": PERSONAL,
    "CYCLES": CYCLES,
    "CLIENT_RECORD": CLIENT_RECORD,
    "PROTOCOL_ADAPTER": PROTOCOL_ADAPTER,
    "xvVaultUSDCV2": xvVaultUSDCV2,
    "xvVaultUSDTV2": xvVaultUSDTV2,
    "xvVaultBUSDV2": xvVaultBUSDV2,
    "xvAutoBSCBUSDV2": xvAutoBSCBUSDV2,
    "xvAutoBSCUSDCV2": xvAutoBSCUSDCV2,
    "xvAutoBSCUSDTV2": xvAutoBSCUSDTV2,
    "xvAutoBSCBNBV2": xvAutoBSCBNBV2,
    "xvAutoUSDCV2Matic": xvAutoUSDCV2Matic,
    "xvAutoUSDTV2Matic": xvAutoUSDTV2Matic,
    "xvAutoAAVEV2Matic": xvAutoAAVEV2Matic,
    "xvAutoWBTCV2Matic": xvAutoWBTCV2Matic,
    "XAUTO": XAUTO,
    "XVAULT": XVAULT,
    "ERC20": ERC20,
    "testnet": {
        "esusu_service": ESUSU_SERVICE,
        "groups": GROUPS,
        "fortubeAdapter": FADAPTER,
    },
}
