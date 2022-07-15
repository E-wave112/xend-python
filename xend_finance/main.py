from xend_finance.strategies.group.group_index import Group
from xend_finance.strategies.individual.individual_index import Personal
from xend_finance.strategies.xauto.auto import Xauto
from xend_finance.strategies.xvault.vault import Xvault

# from xend_finance.utils.balance import get_balance
# from xend_finance.utils.constants.chain_id import ChainId
from xend_finance.models.schemas import Options
from xend_finance.utils.helpers import check_chain_id
from xend_finance.utils.protocol_selector import protocol_selector


default_options: Options = {"env": "testnet"}


class XendFinance:
    def __init__(self, chain_id: int, private_key: str, options=default_options):
        selector = protocol_selector(options)
        chain_data = check_chain_id(chain_id)
        self.chain_id = chain_id
        self.private_key = private_key
        self.options = options
        self.provider = chain_data["url"]
        self.currency = chain_data["currency"]
        self.protocol = selector["name"]
        # self.layer2_addresses = self.get_layer2_addresses()
        self.addresses = selector["addresses"]
        self.share_currency = selector["addresses"].PROTOCOL_CURRENCY
        self.available_protocols = selector["available"]
        # self.cooperative_cycles = self.get_cooperative_cycles()
        # self.esusu_cycles = self.get_esusu_cycles()
        self.xauto = Xauto(self.options.layer2, self.chain_id, self.private_key)
        self.xvault = Xvault(self.options.layer2, self.chain_id, self.private_key)
        self.group = Group(self.provider, self.private_key, self.addresses)
        self.personal = Personal(
            self.provider, self.private_key, self.options, self.addresses, self.protocol
        )

    pass
