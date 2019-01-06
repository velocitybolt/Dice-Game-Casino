#!/usr/bin/python3 
# Author: Murtaza Meerza

contract_data = {'bin': '60606040526000600555341561001457600080fd5b336000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555061007033610075640100000000026101db176401000000009004565b610324565b60008090505b6005548110156100fd5760018160048110151561009457fe5b0160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff16141515156100f057600080fd5b808060010191505061007b565b6000600160055460048110151561011057fe5b0160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1614151561015157fe5b81600160055460048110151561016357fe5b0160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055506001600554016005819055507f7c30c46017e6377826c6557f0d89e6760aced7a4ca61f469b1d729c50a81397c82604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390a1600460055414156102385761023761023c6401000000000261038f176401000000009004565b5b5050565b600080600460055414151561024d57fe5b6004426040518082815260200191505060405180910390206001900481151561027257fe5b06915060018260048110151561028457fe5b0160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1690507ff4ec34d629bd19fe7c2b2142541d4574ed8b77466f7dc5acc7eb1e83ed66441a81604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390a18073ffffffffffffffffffffffffffffffffffffffff16ff5b6104a3806103336000396000f30060606040526000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff1680633a245f3d1461005e5780638da5cb5b146100c157806393950a6a1461011657806393e84cd91461013f57600080fd5b341561006957600080fd5b61007f6004808035906020019091905050610149565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b34156100cc57600080fd5b6100d461017e565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b341561012157600080fd5b6101296101a3565b6040518082815260200191505060405180910390f35b6101476101a9565b005b60018160048110151561015857fe5b016000915054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b60055481565b67016345785d8a0000341415156101bf57600080fd5b60046005541015156101d057600080fd5b6101d9336101db565b565b60008090505b600554811015610263576001816004811015156101fa57fe5b0160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff161415151561025657600080fd5b80806001019150506101e1565b6000600160055460048110151561027657fe5b0160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff161415156102b757fe5b8160016005546004811015156102c957fe5b0160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055506001600554016005819055507f7c30c46017e6377826c6557f0d89e6760aced7a4ca61f469b1d729c50a81397c82604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390a16004600554141561038b5761038a61038f565b5b5050565b60008060046005541415156103a057fe5b600442604051808281526020019150506040518091039020600190048115156103c557fe5b0691506001826004811015156103d757fe5b0160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1690507ff4ec34d629bd19fe7c2b2142541d4574ed8b77466f7dc5acc7eb1e83ed66441a81604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390a18073ffffffffffffffffffffffffffffffffffffffff16ff00a165627a7a723058208bd113077a37a6eec97c5f41d7355a5b05688a49ec45682cb1aa74776c104e010029', 'abi': '[{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"played","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"num_played","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"play","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"name":"player","type":"address"}],"name":"Played","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"player","type":"address"}],"name":"Won","type":"event"}]', 'hashes': {'play()': '93e84cd9', 'played(uint256)': '3a245f3d', 'owner()': '8da5cb5b', 'num_played()': '93950a6a'}}

import sys

from web3 import Web3, HTTPProvider, IPCProvider
from pprint import pprint
import json

# web3 = Web3 (HTTPProvider ("http://localhost:8545"))
web3 = Web3(HTTPProvider ("http://localhost:9545"))

##################################################################

def get_abi (contract):
    abi = json.loads (contract["abi"])
    return abi

##################################################################

def play (contract, account):
    transaction_hash = contract.transact ({
        "from": account,
        "value": web3.toWei (0.1, "ether")
    }).play ()
    print ("transaction hash = {:s}".format (transaction_hash))
    transaction_receipt = web3.eth.getTransactionReceipt (transaction_hash)
    transaction = web3.eth.getTransaction (transaction_hash)
    pprint (transaction_receipt)

##################################################################

contract_address = sys.argv[1]
account_index = int (sys.argv[2])
account = web3.eth.accounts[account_index]

print ("Using account {:d} with address {:s} to play on contract {:s}".format (account_index, account, contract_address))
       
abi = get_abi (contract_data)
contract = web3.eth.contract (abi = abi, address = contract_address)

play (contract, account)
