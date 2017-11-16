#!/usr/bin/python3

contract_data = {'bin': '606060405260006005556001600660014303406001900481151561001f57fe5b066001600660014303406001900481151561003657fe5b06010101600655341561004857600080fd5b336000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055506100a4336100a964010000000002610393176401000000009004565b6103bb565b60008090505b600554811015610131576001816004811015156100c857fe5b0160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff161415151561012457600080fd5b80806001019150506100af565b6000600160055460048110151561014457fe5b0160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1614151561018557fe5b81600160055460048110151561019757fe5b0160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055506001600554016005819055507f7c30c46017e6377826c6557f0d89e6760aced7a4ca61f469b1d729c50a81397c82604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390a16004600554141561026d5761026b61027164010000000002610249176401000000009004565b505b5050565b60006001600260065481151561028357fe5b061415610350577ff4ec34d629bd19fe7c2b2142541d4574ed8b77466f7dc5acc7eb1e83ed66441a33604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390a13373ffffffffffffffffffffffffffffffffffffffff166108fc60023073ffffffffffffffffffffffffffffffffffffffff1631029081150290604051600060405180830381858888f19350505050151561034757600080fd5b600190506103b8565b7f85a3875b3a6e376ada779e06d99beed4fbf471788c1d2719f27718958bfc826b33604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390a1600090505b90565b610574806103ca6000396000f30060606040523615610076576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff16806302d05d3f1461007b5780633a245f3d146100d057806393950a6a1461013357806393e84cd91461015c578063c30e8a2714610166578063c3b61ff41461018f575b600080fd5b341561008657600080fd5b61008e6101b1565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b34156100db57600080fd5b6100f160048080359060200190919050506101d6565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b341561013e57600080fd5b61014661020b565b6040518082815260200191505060405180910390f35b610164610211565b005b341561017157600080fd5b610179610243565b6040518082815260200191505060405180910390f35b610197610249565b604051808215151515815260200191505060405180910390f35b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b6001816004811015156101e557fe5b016000915054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b60055481565b67016345785d8a00003414151561022757600080fd5b600460055410151561023857600080fd5b61024133610393565b565b60065481565b60006001600260065481151561025b57fe5b061415610328577ff4ec34d629bd19fe7c2b2142541d4574ed8b77466f7dc5acc7eb1e83ed66441a33604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390a13373ffffffffffffffffffffffffffffffffffffffff166108fc60023073ffffffffffffffffffffffffffffffffffffffff1631029081150290604051600060405180830381858888f19350505050151561031f57600080fd5b60019050610390565b7f85a3875b3a6e376ada779e06d99beed4fbf471788c1d2719f27718958bfc826b33604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390a1600090505b90565b60008090505b60055481101561041b576001816004811015156103b257fe5b0160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168273ffffffffffffffffffffffffffffffffffffffff161415151561040e57600080fd5b8080600101915050610399565b6000600160055460048110151561042e57fe5b0160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1614151561046f57fe5b81600160055460048110151561048157fe5b0160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055506001600554016005819055507f7c30c46017e6377826c6557f0d89e6760aced7a4ca61f469b1d729c50a81397c82604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390a16004600554141561054457610542610249565b505b50505600a165627a7a72305820ea6f1233be2432d59c95d485b52286993323cc9ab742ada64a67c89efaa42f8c0029','abi':'[{\"constant\":true,\"inputs\":[],\"name\":\"creator\",\"outputs\":[{\"name\":\"\",\"type\":\"address\"}],\"payable\":false,\"stateMutability\":\"view\",\"type\":\"function\"},{\"constant\":true,\"inputs\":[{\"name\":\"\",\"type\":\"uint256\"}],\"name\":\"played\",\"outputs\":[{\"name\":\"\",\"type\":\"address\"}],\"payable\":false,\"stateMutability\":\"view\",\"type\":\"function\"},{\"constant\":true,\"inputs\":[],\"name\":\"num_played\",\"outputs\":[{\"name\":\"\",\"type\":\"uint256\"}],\"payable\":false,\"stateMutability\":\"view\",\"type\":\"function\"},{\"constant\":false,\"inputs\":[],\"name\":\"play\",\"outputs\":[],\"payable\":true,\"stateMutability\":\"payable\",\"type\":\"function\"},{\"constant\":true,\"inputs\":[],\"name\":\"dice_sum\",\"outputs\":[{\"name\":\"\",\"type\":\"uint256\"}],\"payable\":false,\"stateMutability\":\"view\",\"type\":\"function\"},{\"constant\":false,\"inputs\":[],\"name\":\"dicePlay\",\"outputs\":[{\"name\":\"result\",\"type\":\"bool\"}],\"payable\":true,\"stateMutability\":\"payable\",\"type\":\"function\"},{\"inputs\":[],\"payable\":false,\"stateMutability\":\"nonpayable\",\"type\":\"constructor\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":false,\"name\":\"player\",\"type\":\"address\"}],\"name\":\"Played\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":false,\"name\":\"player\",\"type\":\"address\"}],\"name\":\"Won\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":false,\"name\":\"player\",\"type\":\"address\"}],\"name\":\"Lost\",\"type\":\"event\"}]','hashes': {'play()': '93e84cd9', 'played(uint256)': '3a245f3d', 'owner()': '8da5cb5b', 'num_played()': '93950a6a'}}

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
