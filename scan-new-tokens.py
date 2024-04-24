'''
Detect New Pools Created on Solana Raydium DEX

Feel free to email me at hackthatcoffee@gmail.com if you want the full code!

'''

import asyncio
import sys

import websockets
import json
import pandas as pd
from tabulate import tabulate

wallet_address = "675kPX9MHTjS2zt1qfr1NYHuzeLXfQM9H24wFSUt1Mp8"
seen_signatures = set()
solana_client = Client("https://api.mainnet-beta.solana.com")
sol_token = 'So11111111111111111111111111111111111111112'

def getTokens(str_signature):