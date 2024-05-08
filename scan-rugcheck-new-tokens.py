'''
Detect New Pools Created on Solana Raydium DEX

Use RugChecker.xyz to do some initial checking

Feel free to email me at hackthatcoffee@gmail.com if you have questions!
'''

import asyncio
import sys

import websockets
import json
from solana.rpc.api import Client
from solders.pubkey import Pubkey
from solders.signature import Signature
import pandas as pd
import requests
from tabulate import tabulate

wallet_address = "675kPX9MHTjS2zt1qfr1NYHuzeLXfQM9H24wFSUt1Mp8"
seen_signatures = set()
solana_client = Client("https://api.mainnet-beta.solana.com")
sol_token = 'So11111111111111111111111111111111111111112'

def getTokens(str_signature):
    signature = Signature.from_string(str_signature)