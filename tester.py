from web3 import Web3

url = "http://127.0.0.1:8545"
eth_url = "https://eth-mainnet.alchemyapi.io/v2/2gdCD03uyFCNKcyEryqJiaPNtOGdsNLv"
bsc_main_url = "https://bsc-dataseed.binance.org/"
bsc_test_url = "https://data-seed-prebsc-1-s1.binance.org:8545/"
polygon_main_url = "https://rpc-mainnet.matic.network"
polygon_test_url = "https://rpc-mumbai.matic.today"

get_address = Web3(Web3.HTTPProvider(url))

balance = get_address.eth.getBalance("0x94f6f0E5a7923b5C38083Dec91eC3b037f251A20")

balance_to_ether = get_address.fromWei(balance, "ether")
print(balance_to_ether)

# get the eth address from the private key and node url
get_eth_address = get_address.eth.account.from_key(
    "0x1e7af0beb946cec7c343a66e8a39856585d9679dcd6dd3c5468bb3a1ee57778a"
)
print(len(get_eth_address.address))
