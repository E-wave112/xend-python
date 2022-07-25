# Xend-python SDK

![PyPI](https://img.shields.io/pypi/v/xend_python_sdk)  ![PyPI - License](https://img.shields.io/pypi/l/xend-python-sdk) ![PyPI - Downloads](https://img.shields.io/pypi/dm/xend-python-sdk)


The Xend Finance SDK arms python developers with the ability to build DeFi applications with [Xend Finance](https://xend.finance/) without needing to understand the complexities of the underlying blockchain or layer2 infrastructure.

## Table of content

- [Want to Contribute](#want-to-contribute)
- [Installation](#installation)
- [Usage](#usage)
- [Available Strategies exposed by the SDK](#available-strategies-exposed-by-the-sdk)


## Want to contribute?

Contributions are welcome! Kindly refer to the [contribution guidelines](https://github.com/E-wave112/xend-python/blob/main/CONTRIBUTING.md).

## Installation

To install this sdk, run the command:

```
pip install xend_python_sdk
```

## Usage

```py
import xend_finance
from xend_finance.main import XendFinance
```

Instantiate the XendFinance class like so:

```py
xend = XendFinance(your_chain_id, private_key,  {"env": "testnet"})
```

You can use Xend Finance in as many scenario's you can come up with, but there are 2 examples
1. Use one general address for all your transactions
2. Create a new address for each of your users and use for their transactions

**Note:**

- The env field is one of ```local```, ```testnet``` and ```mainnet```.
- the chain_id of the network. a chain id of 1 represents the ethereum mainnet, 56 represents the Binance Smart Chain(BSC) mainnet, 137 represents the polygon mainnet while 0 denotes a localnet.

#### Protocol Type
This is the structure of a protocol to be used by the SDK and will be helpful when using the SDK on your local machine with an instance of tools like ganache.

```json
{
  "name":"",
  "code":"",
  "addresses": {
    "PROTOCOL_ADAPTER": "",
    "PROTOCOL_SERVICE": "",
    "GROUPS": "",
    "CYCLES": "",
    "ESUSU_SERVICE": "",
    "ESUSU_STORAGE": "",
    "ESUSU_ADAPTER": "",
    "COOPERATIVE": "",
    "PERSONAL": "",
    "CLIENT_RECORD": "",
    "XEND_TOKEN": "",
    "TOKEN": "",
    "PROTOCOL_CURRENCY": "",
  }
}
```


## Available Strategies exposed by the SDK
> Refer to the official [documentation](https://docs.xend.finance) for more information about the exposed strategies

The following services are available with this SDK

**1**. [**General**](#1-general)
- [Create Wallet](#create-wallet)
- [Retrieve Wallet](#retrieve-wallet)
- [Wallet Balance](#wallet-balance)
- [Get PPFS](#get-ppfs)

**2**. [**Personal Savings**](#2-personal-savings)
- [Flexible Deposit](#flexible-deposit)
- [Fixed Deposit](#fixed-deposit)
- [Get fixed deposit record](#get-fixed-deposit-record)
- [Get flexible deposit record](#get-fixed-deposit-record)
- [Fixed Withdrawal](#fixed-withdrawal)
- [Flexible Withdrawal](#flexible-withdrawal)

**3**. [**Esusu**](#3-esusu)
- [Create Esusu Cycle](#create-esusu-cycle)
- [Get Cycles Count](#get-cycles-count)
- [Get Cycle Id](#get-cycle-id)
- [Get Esusu Info](#get-esusu-info)
- [Join Esusu Group](#join-esusu-group)
- [Start Esusu Cycle](#start-esusu-cycle)
- [Withdraw Interest](#withdraw-interest)
- [Withdraw Capital](#withdraw-capital)
- [Is Member](#is-member)
- [Accrue Interest Capital](#accrue-interest-capital)
- [Create Esusu Group](#create-esusu-group)
- [Get Esusu Group](#get-esusu-group)
- [Esusu Contributions](#esusu-contributions)
- [No of Contributions](#no-of-contributions)
- [Get cycles in group](#get-cycles-in-group)

**4**. [**Cooperative Savings**](#4-cooperative-savings)

- [Create Cooperative Cylce](#create-cooperative-cycle)
- [Join Cooperative Cycle](#join-cooperative-cycle)
- [Get Cooperative Info](#get-cooperative-info)
- [Is Cooperative Member](#is-cooperative-member)
- [Start Cooperative Cycle](#start-cooperative-cycle)
- [Withdraw From Ongoing Cycle](#withdraw-from-ongoing-cycle)
- [Withdraw From Completed Cycle](#withdraw-from-completed-cycle)
- [Create Cooperative Group](#create-cooperative-group)
- [Get Cooperative Group](#get-cooperative-group)
- [Cooperative Contributions](#cooperative-contributions)
- [Cooperative cycles in group](#cooperative-cycles-in-group)

**5**. [**Groups**](#5-groups)
- [Create Group](#create-group)
- [Get Group](#get-group)
- [Get Groups](#get-groups)
- [Get rewards](#get-rewards)

**6**. [**Xauto**](#6-xauto)
- [Approve](#approve)
- [Deposit](#deposit)
- [Withdraw](#withdraw)
- [Get Price per share](#get-price-per-share)
- [Share Balance](#share-balance)

**7**. [**Xvault**](#7-xvault)
- [Approve vault](#approve-vault)
- [Deposit vault](#deposit-vault)
- [Withdraw vault](#withdraw-vault)
- [Get Price per share vault](#get-price-per-share-vault)
- [Share Balance vault](#share-balance-vault)


### 1. General

This strategy provides utility methods such as creating a wallet, getting wallet balance and getting price per full share.

#### Create Wallet

This method allows a user to create a wallet on a specific node.

```py
create_wallet = xend.create_wallet()
```

#### Retrieve Wallet

This method allows a user retrieve the details of a wallet such as wallet address and private key.

```py
retrieve_wallet = xend.retrieve_wallet()
```

#### Wallet Balance

This method allows a user retrieve the balance details of a wallet

```py
 wallet_balance = xend.wallet_balance()
```

#### Get PPFS

This method allows a user retrieve the price per full share of his/her wallet

```py
get_ppfs = xend.get_ppfs()
```

### 2. Personal Savings

This strategy provides methods for users to interact with their savings from Xend finance.

#### Flexible Deposit

This method allows users to create a flexible deposit on their wallet

```py
create_flexible_deposit = xend.personal.flexible_deposit("20")
```

#### Parameters supported

| **Parameters**  | **Data type** | **Required** | **Description**                 |
| --------------- | ------------- | ------------ | ------------------------------- |
| `deposit_amount`    | string       | true         | The amount to be deposited. |


#### Fixed Deposit

This method allows users to create a fixed deposit on their wallet for a specific period of time

```py
create_fixed_deposit = xend.personal.fixed_deposit("40", 30000)
```

#### Parameters supported

| **Parameters**  | **Data type** | **Required** | **Description**                 |
| --------------- | ------------- | ------------ | ------------------------------- |
| `deposit_amount`    | string       | true         | The amount to be deposited. |
| `lock_period`    | integer      | true         | The lock period in seconds. |


#### Get fixed deposit record

This method allows users to get a list of all fixed deposits on their wallet

```py
fixed_deposit_record = xend.personal.get_fixed_deposit_record()
```

#### Get flexible deposit record

This method allows users to get a list of all flexible deposits on their wallet

```py
flexible_deposit_record = xend.personal.get_flexible_deposit_record()
```

#### Fixed Withdrawal

This method allows users to perform fixed withdrawals on their wallet

```py
fixed_withdrawal = xend.personal.fixed_withdrawal(10)
```

#### Parameters supported

| **Parameters**  | **Data type** | **Required** | **Description**                 |
| --------------- | ------------- | ------------ | ------------------------------- |
| `record_id`    | string       | true         | The id of the savings to be withdrawn from. |


#### Flexible Withdrawal

This method allows users to perform flexible withdrawals on their wallet

```py
flexible_withdrawal = xend.personal.flexible_withdrawal("30.0")
```

#### Parameters supported

| **Parameters**  | **Data type** | **Required** | **Description**                 |
| --------------- | ------------- | ------------ | ------------------------------- |
| `amount`    | string or float       | true         | The amount a user wants to withdraw. |


### 3. Esusu

This strategy provides methods for users to interact with an esusu style of contributions/savings from Xend finance.

#### Create Esusu Cycle

This method allows users to create esusu cycles

```py
args = {
    "group_id": 1,
    "deposit_amount": "300",
    "payout_interval_in_seconds": 3600,
    "start_time_in_seconds": 1579014400,
    "max_members": 10
}
create_esusu_cycle = xend.esusu.create_esusu(args)
```

#### Parameters supported

| **Parameters**  | **Data type** | **Required** | **Description**                 |
| --------------- | ------------- | ------------ | ------------------------------- |
| `group_id`    | integer       | true         | The group a user wants to create the cycle on |
| `deposit_amount`    | string      | true         | The amount a user wants to deposit while creating the cycle |
| `payout_interval_in_seconds`    | integer      | true         | The payout interval in seconds. |
| `start_time_in_seconds`    | integer       | true         | The start time in seconds. |
| `max_members`    | integer       | true         | The maximum number of members in the cycle. |


#### Get Cycles Count

This method returns the number of esusu cycles a user has/is present in

```py
get_esusu_cycles_count = xend.esusu.get_cycles_count()
```

#### Get Cycle Id

This method returns the cycle id of a cycle at the specified position in the list of cycles created by the user

```py
get_esusu_cycle_id = xend.esusu.get_cycle_id_from_cycles_created(6)
```

#### Parameters supported

| **Parameters**  | **Data type** | **Required** | **Description**                 |
| --------------- | ------------- | ------------ | ------------------------------- |
| `position`    | integer       | true         | The position of the cycle |


#### Get Esusu Info

This method returns the information about an esusu cycle/group

```py
get_esusu_info = xend.esusu.get_esusu_info(5)
```


#### Parameters supported

| **Parameters**  | **Data type** | **Required** | **Description**                 |
| --------------- | ------------- | ------------ | ------------------------------- |
| `esusu_id`    | integer       | true         | The id of the esusu group/cycle |


#### Join Esusu Group

This method allows users to join an esusu group or cycle

```py
join_esusu_cycle = xend.esusu.join(9)
```

#### Parameters supported

| **Parameters**  | **Data type** | **Required** | **Description**                 |
| --------------- | ------------- | ------------ | ------------------------------- |
| `id`    | integer       | true         | The id of the esusu group/cycle |


#### Start Esusu Cycle
This method allows users to start an esusu cycle

```py
start_esusu_cycle = xend.esusu.start(3)
```

#### Parameters supported

| **Parameters**  | **Data type** | **Required** | **Description**                 |
| --------------- | ------------- | ------------ | ------------------------------- |
| `cycle_id`    | integer       | true         | The id of the esusu cycle |

#### Withdraw Interest
This method allows users to withdraw their interest from an esusu group/cycle

```py
withdraw_interest = xend.esusu.withdraw_interest(8)
```

#### Parameters supported

| **Parameters**  | **Data type** | **Required** | **Description**                 |
| --------------- | ------------- | ------------ | ------------------------------- |
| `esusu_id`    | integer       | true         | The id of the esusu group/cycle |


#### Withdraw Capital
This method allows users to withdraw their capital from an esusu group/cycle

```py
withdraw_capital = xend.esusu.withdraw_capital(14)
```

#### Parameters supported

| **Parameters**  | **Data type** | **Required** | **Description**                 |
| --------------- | ------------- | ------------ | ------------------------------- |
| `esusu_id`    | integer       | true         | The id of the esusu group/cycle |

#### Is Member
This method checks if a particular user is in an esusu cycle

```py
is_member_of_esusu_cycle = xend.esusu.is_member_of_cycle(9)
```

#### Parameters supported

| **Parameters**  | **Data type** | **Required** | **Description**                 |
| --------------- | ------------- | ------------ | ------------------------------- |
| `cycle_id`    | integer       | true         | The id of the esusu cycle |


#### Accrue Interest Capital
This method returns the accrued interest and capital of a user from an esusu cycle

```py
get_interest_capital = xend.esusu.accrue_interest_capital(16)
```

#### Parameters supported

| **Parameters**  | **Data type** | **Required** | **Description**                 |
| --------------- | ------------- | ------------ | ------------------------------- |
| `cycle_id`    | integer       | true         | The id of the esusu cycle |

#### Create Esusu Group
This methods allows users to create an esusu group

```py
create_esusu_group = xend.esusu.create_group('test', 'TXT')
```

#### Parameters supported

| **Parameters**  | **Data type** | **Required** | **Description**                 |
| --------------- | ------------- | ------------ | ------------------------------- |
| `group_name`    | string       | true         | The name of the group |
| `symbol`    | string      | true         | The group's symbol |


#### Get Esusu Group
This method returns all the esusu groups a user is associated with

```py
get_esusu_group = xend.esusu.get_groups()
```

#### Esusu Contributions
This methods returns all the contributions a user has made in the esusu groups/cycles he is associated with

```py
esusu_contributions = xend.esusu.contributions()
```

#### No Of Contributions
This methods returns the contributions count of a user in the groups/cycles he is associated with

```py
no_of_contributions = xend.esusu.no_of_contributions()
```

#### Get cycles in Group
This method returns the esusu cycles present in a particular esusu group

```py
esusu_cycles_in_group = xend.esusu.cycles_in_group(11)
```

#### Parameters supported

| **Parameters**  | **Data type** | **Required** | **Description**                 |
| --------------- | ------------- | ------------ | ------------------------------- |
| `group_id`    | integer       | true         | The id of the esusu group |


### 4. Cooperative Savings

This strategy provides methods for users to interact with cooperative savings and contributions from Xend finance.

#### Create Cooperative Cycle
This method allows users to create cooperative cycles

```py
args = {
    "group_id": 1,
    "cycle_stake_amount": "0.1",
    "payout_interval_in_seconds": 3600,
    "start_time_in_seconds": 1579014400,
    "max_members": 10
}
create_cooperate = xend.cooperative.create(args)
```

#### Parameters supported

| **Parameters**  | **Data type** | **Required** | **Description**                 |
| --------------- | ------------- | ------------ | ------------------------------- |
| `group_id`    | integer       | true         | The group the user wants to create the cycle on |
| `cycle_stake_amount`    | string      | true         | The stake amount the user wants to deposit while creating the cycle |
| `payout_interval_in_seconds`    | integer      | true         | The payout interval in seconds. |
| `start_time_in_seconds`    | integer       | true         | The start time in seconds. |
| `max_members`    | integer       | true         | The maximum number of members in the cycle. |

#### Join Cooperative Cycle
This method allows users to join a cooperative cycle

```py
join_cooperative = xend.cooperative.join(10,25)
```

#### Parameters supported

| **Parameters**  | **Data type** | **Required** | **Description**                 |
| --------------- | ------------- | ------------ | ------------------------------- |
| `cycle_id`    | integer       | true         | The id of to the cooperative cycle|
| `number_of_stakes`    | integer      | true         | The stake amount the user wants to deposit while joining the cycle |


#### Get Cooperative Info


This method returns the information about a cooperatve cycle

```py
cooperative_cycle_info = xend.cooperative.info(5)
```

#### Parameters supported

| **Parameters**  | **Data type** | **Required** | **Description**                 |
| --------------- | ------------- | ------------ | ------------------------------- |
| `cycle_id`    | integer       | true         | The id of to the cooperative cycle|

#### Is Cooperative Member

This method checks if a particular user is in a cooperative cycle

```py
does_member_exist = xend.cooperative.cycle_member_exist(5)
```

#### Parameters supported

| **Parameters**  | **Data type** | **Required** | **Description**                 |
| --------------- | ------------- | ------------ | ------------------------------- |
| `cycle_id`    | integer       | true         | The id of to the cooperative cycle|

#### Start Cooperative Cycle

This method allows users to start a cooperative cycle

```py
start_cycle = xend.cooperative.start_cyle(5)
```

#### Parameters supported

| **Parameters**  | **Data type** | **Required** | **Description**                 |
| --------------- | ------------- | ------------ | ------------------------------- |
| `cycle_id`    | integer       | true         | The id of to the cooperative cycle|

#### Withdraw From Ongoing Cycle
This method allows users to withdraw tokens from an ongoing cooperative cycle

```py
withdraw_ongoing_cycle = xend.cooperative.withdraw_from_ongoing_cycle(7)
```

#### Parameters supported

| **Parameters**  | **Data type** | **Required** | **Description**                 |
| --------------- | ------------- | ------------ | ------------------------------- |
| `cycle_id`    | integer       | true         | The id of to the cooperative cycle|

#### Withdraw From Completed Cycle
This method allows users to withdraw tokens from a completed cooperative cycle

```py
withdraw_completed_cycle = xend.cooperative.withdraw_completed(10)
```

#### Parameters supported

| **Parameters**  | **Data type** | **Required** | **Description**                 |
| --------------- | ------------- | ------------ | ------------------------------- |
| `cycle_id`    | integer       | true         | The id of to the cooperative cycle|

#### Create Cooperative Group
This method allows users to create a cooperative group

```py
create_cooperative_group = xend.cooperative.create_group('test', 'TST')
```

#### Parameters supported

| **Parameters**  | **Data type** | **Required** | **Description**                 |
| --------------- | ------------- | ------------ | ------------------------------- |
| `group_name`    | string       | true         | The name of the group |
| `symbol`    | string      | true         | The group's symbol |

#### Get Cooperative Group

This method returns all the cooperative groups a user is associated with

```py
get_cooperative_groups = xend.cooperative.get_cooperative_groups()
```

#### Cooperative Contributions

This methods returns all the contributions a user has made in the cooperative groups/cycles he is associated with

```py
cooperative_cycles_contributions = xend.cooperative.contributions()
```

#### Cooperative cycles in group

This method returns the cooperative cycles present in a particular cooperative group

```py
cycles_in_cooperative_group = xend.cooperative.cycles_in_group(1)
```


#### Parameters supported

| **Parameters**  | **Data type** | **Required** | **Description**                 |
| --------------- | ------------- | ------------ | ------------------------------- |
| `group_id`    | integer       | true         | The id of the cooperative group |


### 5. Groups

This strategy provides utility methods for groups related operations such as creating a group, getting a group/groups and getting group rewards

#### Create Group

This method allows a user to create a group.

```py
create_group = xend.group.create('mnt', 'MNT')
```

#### Parameters supported

| **Parameters**  | **Data type** | **Required** | **Description**                 |
| --------------- | ------------- | ------------ | ------------------------------- |
| `group_name`    | string       | true         | The name of the group |
| `symbol`    | string      | true         | The group's symbol |

#### Get Group

This method allows a user retrieve the details of a group.

```py
get_single_group = xend.group.get_single_group(3)
```

#### Parameters supported

| **Parameters**  | **Data type** | **Required** | **Description**                 |
| --------------- | ------------- | ------------ | ------------------------------- |
| `group_id`    | integer       | true         | The id of the cooperative group |

#### Get Groups

This method returns all the groups a user is associated with

```py
get_groups = xend.group.get_groups()
```

#### Get rewards

This method allows a user redeem any xend rewards earned

```py
get_xend_rewards = xend.group.get_xend_rewards()
```

### 6. Xauto

This strategy provides utility methods for auto yield related operations on the xAuto protocol.

#### Approve
This method approves the amount of tokens to be spent from a user's wallet

```py
approve_token = xend.xauto.approve("TNT", 300)
```

#### Parameters supported
| **Parameters**  | **Data type** | **Required** | **Description**                 |
| --------------- | ------------- | ------------ | ------------------------------- |
| `token`    | string       | true         | The token to be approved |
| `amount`    | integer      | true         | The amount of tokens to be approved |

#### Deposit
This method deposits an amount of tokens to a user's wallet

```py
deposit_token = xend.xauto.deposit("BSC",150)
```

#### Parameters supported

| **Parameters**  | **Data type** | **Required** | **Description**                 |
| --------------- | ------------- | ------------ | ------------------------------- |
| `token`    | string       | true         | The token to be deposited |
| `amount`    | integer      | true         | The amount of tokens to be deposited |

#### Withdraw
This method withdraws an amount of tokens from a user's wallet

```py
withdraw_token = xend.xauto.withdraw("DAI",240)
```

#### Parameters supported

| **Parameters**  | **Data type** | **Required** | **Description**                 |
| --------------- | ------------- | ------------ | ------------------------------- |
| `token`    | string       | true         | The token to be withdrawn |
| `amount`    | integer      | true         | The amount of tokens to be withdrawn |

#### Get Price per Share
This method returns the price per share of a token

```py
get_ppfs = xend.xauto.ppfs("DAI")
```

#### Parameters supported

| **Parameters**  | **Data type** | **Required** | **Description**                 |
| --------------- | ------------- | ------------ | ------------------------------- |
| `token`    | string       | true         | The token name |

#### Share Balance
This method returns the balance of a token in a user's wallet

```py
get_share_balance = xend.xauto.share_balance("DAI")
```
#### Parameters supported
| **Parameters**  | **Data type** | **Required** | **Description**                 |
| --------------- | ------------- | ------------ | ------------------------------- |
| `token`    | string       | true         | The token name |

### 7. Xvault

This strategy provides utility methods for auto yield related operations  on the xVault protocol

#### Approve vault
This method approves the amount of tokens to be spent from a user's wallet

```py
approve_token = xend.xvault.approve("BSC", 250)
```

#### Parameters supported
| **Parameters**  | **Data type** | **Required** | **Description**                 |
| --------------- | ------------- | ------------ | ------------------------------- |
| `token`    | string       | true         | The token to be approved |
| `amount`    | integer      | true         | The amount of tokens to be approved |

#### Deposit vault
This method deposits an amount of tokens to a user's wallet

```py
deposit_token = xend.xvault.deposit("BSC",150)
```

#### Parameters supported

| **Parameters**  | **Data type** | **Required** | **Description**                 |
| --------------- | ------------- | ------------ | ------------------------------- |
| `token`    | string       | true         | The token to be deposited |
| `amount`    | integer      | true         | The amount of tokens to be deposited |

#### Withdraw vault
This method withdraws an amount of tokens from a user's wallet

```py
withdraw_token = xend.xvault.withdraw("DAI",240)
```

#### Parameters supported

| **Parameters**  | **Data type** | **Required** | **Description**                 |
| --------------- | ------------- | ------------ | ------------------------------- |
| `token`    | string       | true         | The token to be withdrawn |
| `amount`    | integer      | true         | The amount of tokens to be withdrawn |

#### Get Price per Share vault
This method returns the price per share of a token

```py
get_ppfs = xend.xvault.ppfs("DAI")
```

#### Parameters supported

| **Parameters**  | **Data type** | **Required** | **Description**                 |
| --------------- | ------------- | ------------ | ------------------------------- |
| `token`    | string       | true         | The token name |

#### Share Balance vault
This method returns the balance of a token in a user's wallet

```py
get_share_balance = xend.xvault.share_balance("DAI")
```
#### Parameters supported
| **Parameters**  | **Data type** | **Required** | **Description**                 |
| --------------- | ------------- | ------------ | ------------------------------- |
| `token`    | string       | true         | The token name |