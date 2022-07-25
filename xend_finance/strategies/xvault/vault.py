import math
from typing import List, Any

from xend_finance.strategies.contract import getContract
from xend_finance.utils.exceptions.handleErrors import BaseError
from xend_finance.utils.helpers import check_chain_id, format_amount
from xend_finance.utils.key_address import private_key_to_address
from xend_finance.utils.send_signed_transaction import send_signed_transaction


class Xvault:
    """
    Class that allows users to access Xvault related functions
    """

    protocol = "xVault"

    def __init__(self, assets: List[Any], chain_id: int, private_key: str):
        self.assets = assets
        self.chain_id = chain_id
        self.private_key = private_key
        self.rpc = check_chain_id(chain_id)["url"]

    def approve(self, token_name: str, amount: int):
        """
        It approves the amount of tokens to be spent on the smart contract

        :param token_name: The name of the token you want to approve
        :type token_name: str
        :param amount: The amount of tokens to be approved
        :type amount: int
        :return: The transaction hash is being returned.
        """
        try:
            results = self.filter_token(token_name, self.chain_id, self.protocol)
            if not results:
                raise BaseError({"message": "Token not found"})

            approval_amount = format_amount(amount, self.chain_id, token_name)
            contract = getContract(
                self.rpc, results["tokenAbi"], results["tokenAddress"]
            )
            # approve the amount of tokens to be spent on the smart contract
            tx = contract.functions.approve(
                results["protocolAddress"], approval_amount
            ).transact()
            #  get the transaction hash
            transaction_hash = send_signed_transaction(
                self.private_key,
                self.rpc,
                tx,
                contract,
                results["tokenAddress"],
                "approve",
            )
            return transaction_hash
        except BaseError as e:
            raise BaseError(e)

    def deposit(self, token_name: str, amount: int):
        """
        It takes in a token name and an amount, and returns a transaction hash

        :param token_name: The name of the token you want to deposit
        :type token_name: str
        :param amount: The amount of tokens to be deposited
        :type amount: int
        :return: The transaction hash is being returned.
        """
        try:
            results = self.filter_token(token_name, self.chain_id, self.protocol)
            if not results:
                raise BaseError({"message": "Token not found"})

            deposit_amount = format_amount(amount, self.chain_id, token_name)
            contract = getContract(
                self.rpc, results["protocolAbi"], results["protocolAddress"]
            )
            # approve the amount of tokens to be spent on the smart contract
            tx = contract.functions.deposit(deposit_amount).transact()
            #  get the transaction hash
            transaction_hash = send_signed_transaction(
                self.private_key,
                self.rpc,
                tx,
                contract,
                results["protocolAddress"],
                "deposit",
            )
            return transaction_hash
        except BaseError as e:
            raise BaseError(e)

    def withdraw(self, token_name: str, amount: int):
        """
        The function takes in a token name, and an amount, and returns a transaction hash

        :param token_name: The name of the token you want to withdraw
        :type token_name: str
        :param amount: The amount of tokens you want to withdraw
        :type amount: int
        :return: The transaction hash of the withdraw transaction.
        """
        try:
            results = self.filter_token(token_name, self.chain_id, self.protocol)
            if not results:
                raise BaseError({"message": "Token not found"})
            contract = getContract(
                self.rpc, results["protocolAbi"], results["protocolAddress"]
            )
            client_address = private_key_to_address(self.rpc, self.private_key)
            share = contract.functions.balanceOf(client_address).call()
            contract_ppfs = results["ppfsMethod"]
            ppfs = contract.functions[contract_ppfs]
            ppfs_data = ppfs().call({"from": client_address})
            divisor = math.pow(10, results["widthdrawDecimals"])
            total_deposit = float(share) * float(ppfs_data) / divisor
            withdraw_amount = float(share) * float(amount) / total_deposit
            final_withdraw_amount = math.trunc(withdraw_amount)
            tx = contract.functions.withdraw(str(final_withdraw_amount)).transact()
            transaction_hash = send_signed_transaction(
                self.private_key,
                self.rpc,
                tx,
                contract,
                results["protocolAddress"],
                "withdraw",
            )
            return transaction_hash
        except BaseError as e:
            raise BaseError(e)

    def ppfs(self, token_name: str):
        """
        It takes in a token name and returns a transaction hash

        :param token_name: The name of the token you want to deposit
        :type token_name: str
        :return: The transaction hash is being returned.
        """
        try:
            results = self.filter_token(token_name, self.chain_id, self.protocol)
            if not results:
                raise BaseError({"message": "Token not found"})
            contract = getContract(
                self.rpc, results["protocolAbi"], results["protocolAddress"]
            )
            contract_method = results["ppfsMethod"]
            ppfs = contract.functions[contract_method]
            ppfs_data = ppfs().call()
            return ppfs_data
        except BaseError as e:
            raise BaseError(e)

    def share_balance(self, token_name: str):
        """
        This function returns the balance of the token that the user has in the protocol

        :param token_name: The name of the token you want to query
        :type token_name: str
        :return: The balance of the token
        """
        try:
            results = self.filter_token(token_name, self.chain_id, self.protocol)
            if not results:
                raise BaseError({"message": "Token not found"})
            client_address = private_key_to_address(self.rpc, self.private_key)
            contract = getContract(
                self.rpc, results["protocolAbi"], results["protocolAddress"]
            )
            balance = contract.functions.balanceOf(client_address).call()
            return balance
        except BaseError as e:
            raise BaseError(e)

    def filter_token(self, token_name: str, network: int, protocol: str):
        """
        > Filter the assets by token name, network, and protocol

        :param token_name: The name of the token you want to filter by
        :type token_name: str
        :param network: The network you want to use. For example, mainnet, rinkeby, etc
        :type network: str
        :param protocol: the protocol of the token, e.g. "ethereum"
        :type protocol: str
        :return: The first element of the filtered_tokens list.
        """
        # filter assets by token name, network, and protocol
        filtered_tokens = list(
            filter(
                lambda asset: asset["name"] == token_name
                and asset["network"] == network
                and asset["protocolName"] == protocol,
                self.assets,
            )
        )
        if len(filtered_tokens) == 0:
            return None
        return filtered_tokens and filtered_tokens[0]
