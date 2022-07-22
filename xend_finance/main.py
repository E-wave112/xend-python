from xend_finance.strategies.cooperative.cooperative_index import Cooperative
from xend_finance.strategies.esusu.esusu_index import Esusu
from xend_finance.strategies.group.group_index import Group
from xend_finance.strategies.individual.individual_index import Personal
from xend_finance.strategies.xauto.auto import Xauto
from xend_finance.strategies.xvault.vault import Xvault
from xend_finance.models.schemas import Addresses, Options
from xend_finance.utils.balance import get_balance
from xend_finance.utils.get_address import get_bsc_mainnet_addresses, get_layer2_protocols
from xend_finance.utils.helpers import check_chain_id
from xend_finance.utils.price_per_full_share import price_per_full_share
from xend_finance.utils.protocol_selector import protocol_selector
from xend_finance.utils.web3_utils import create_wallet, retrieve_wallet


class XendFinance:
    """
    The main class that is used to interact with the XendFinance API.
    """

    def __init__(self, chain_id: int, private_key: str, options: Options):
        # options.layer2 = get_layer2_protocols()
        chain_data = check_chain_id(chain_id)
        self.chain_id = chain_id
        self.private_key = private_key
        self.options = Options(**options)
        self.options.layer2 = get_layer2_protocols()
        self.options.protocols = get_bsc_mainnet_addresses()
        self.provider = chain_data["url"]
        self.currency = chain_data["currency"]
        selector = protocol_selector(self.options)
        self.protocol = selector["name"]
        addresses_selector: Addresses = Addresses(**selector["addresses"])
        # addresses_selector.PERSONAL = "0x4A37F2aE81AE04dcAF974C245B3d73C8f01C5D46"
        self.addresses = addresses_selector
        self.share_currency = addresses_selector.PROTOCOL_CURRENCY
        self.available_protocols = selector["available"]
        self.xauto = Xauto(self.options.layer2, self.chain_id, self.private_key)
        self.xvault = Xvault(self.options.layer2, self.chain_id, self.private_key)
        self.group = Group(self.provider, self.private_key, self.addresses)
        self.personal = Personal(
            self.provider, self.private_key, self.options, self.addresses, self.protocol
        )
        self.esusu = Esusu(
            self.provider, self.private_key, self.options, self.addresses, self.protocol
        )
        self.cooperative = Cooperative(
            self.provider, self.private_key, self.options, self.addresses, self.protocol
        )

    def create_wallet(self):
        """
        It creates a new wallet for the user
        :return: A wallet object
        """
        return create_wallet(self.chain_id)

    def retrieve_wallet(self):
        """
        `retrieve_wallet` takes a chain_id and a private_key and returns a wallet object
        :return: The wallet object is being returned.
        """
        return retrieve_wallet(self.chain_id, self.private_key)

    def wallet_balance(self):
        """
        `wallet_balance` is a function that takes in a provider, a private key,
        and a list of addresses, and
        returns the balance of the wallet.
        :return: The balance of the wallet.
        """
        return get_balance(self.provider, self.private_key, self.addresses)

    def get_ppfs(self):
        """
        It returns the price per full share of the given provider
        :return: The price per full share of the provider and the protocol adapter.
        """
        return price_per_full_share(self.provider, self.addresses.PROTOCOL_ADAPTER)
