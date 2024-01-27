import hashlib
import json
from time import time
from typing import Optional
from web3 import Web3  # Import Web3 library for Ethereum interactions

class Blockchain:
    def __init__(self, ganache_url: str):
        self.w3 = Web3(Web3.HTTPProvider(ganache_url))
        self.chain = []
        self.current_setpoints = {'Electric': None, 'Boiler_Setpoint': None, 'Ventilation_Setpoint': None}

        # Create the genesis block
        self.new_block(previous_hash='1')

    def new_block(self, previous_hash: Optional[str]) -> dict:
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'setpoints': self.current_setpoints,
            'previous_hash': previous_hash or self.hash(self.chain[-1]) if self.chain else None,
        }

        # Reset current setpoints after adding a block
        self.current_setpoints = {'Electric': None, 'Boiler_Setpoint': None, 'Ventilation_Setpoint': None}

        self.chain.append(block)
        return block

    def add_setpoints(self, electric: float, boiler_setpoint: float, ventilation_setpoint: float):
        self.current_setpoints['Electric'] = electric
        self.current_setpoints['Boiler_Setpoint'] = boiler_setpoint
        self.current_setpoints['Ventilation_Setpoint'] = ventilation_setpoint

    @staticmethod
    def hash(block: dict) -> str:
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
