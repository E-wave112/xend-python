from xend_finance.utils.key_address import private_key_to_address
from xend_finance.utils.web3_utils import initialize_web3


def send_signed_native_transaction(
    private_key: str,
    provider: str,
    tx,
    contract,
    contract_address: str,
    deposit_amount: str,
) -> str:
    """
    This function takes in a private key, a provider, a transaction, a contract,
    a contract address, and
    a deposit amount. It then returns a transaction hash

    :param private_key: The private key of the account that will be sending the transaction
    :type private_key: str
    :param provider: the url of the ethereum node you want to connect to
    :type provider: str
    :param tx: the transaction object
    :param contract: The contract object that we created earlier
    :param contract_address: The address of the contract you want to interact with
    :type contract_address: str
    :param deposit_amount: The amount of token you want to deposit
    :type deposit_amount: str
    :return: The transaction hash is being returned.
    """
    web3 = initialize_web3(provider)
    client_address = private_key_to_address(provider, private_key)
    # get network id
    network_id = web3.net.version
    # get nonce
    nonce = web3.eth.get_transaction_count(client_address)
    # get gas price
    gas_price = web3.eth.gas_price
    # get gas
    gas = tx.estimate_gas(
        {
            "from": client_address,
            "nonce": nonce,
            "gas_price": gas_price,
            "value": deposit_amount,
        }
    )
    encoded_data = contract.encodeABI(fn_name="deposit")
    transaction_data = {
        "from": client_address,
        "nonce": nonce,
        "gasPrice": gas_price,
        "gas": gas,
        "to": contract_address,
        "value": deposit_amount,
        "data": encoded_data,
        "chainId": network_id,
    }
    signed_transaction = web3.eth.sign_transaction(transaction_data, private_key)
    # send the signed transaction
    reciept_for_transaction = web3.eth.send_raw_transaction(
        signed_transaction.rawTransaction
    )
    # convert the transaction hash to readable format and return it
    return web3.toHex(reciept_for_transaction)
