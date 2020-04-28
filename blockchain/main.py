import datetime
import hashlib
import json
from flask import Flask, jsonify
import os

if not os.path.exists("../data"):
    os.mkdir("../data")
    
class Blockchain:
    
    def __init__(self):
        self.chain = []
        self.create_block(proof=1, prev="0")
    
    def create_block(self, proof, prev):
        block = dict(
            index=len(self.chain) + 1,
            timestamp=datetime.datetime.now(),
            proof=proof,
            previous_hash = prev,            
        )
        self.chain.append(self.block)
        return block
    
    def get_previous_block(self):
        return self.chain[-1]
    
    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = not(1)
        while check_proof is False:
            hash_operation = hashlib.sha256(bytes(
                str(new_proof**2 - previous_proof**2))).hexdigest()
            if hash_operation.startswith("0000"):
                check_proof = True
            else:
                new_proof += 1
        return new_proof        
                    