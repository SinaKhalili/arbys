"""
This is a simple script that:

Checks the btc-one price on sushi
Checks the btc-one pair on binance
Checks the bridge
"""
from web3 import Web3
import json
import time
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
from tqdm import tqdm
from web3.contract import BadFunctionCallOutput
import logging
import concurrent.futures
