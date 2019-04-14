import json
import hashlib
from time import time 




class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transaction = []

        #creating a genesis block 
        self.new_block(previous_hash=1, proof=100)





    def new_block(self, prof, previous_hash=None):

        #creation new block and adding
        #parametr proof: <init>
        #parametr previous_hash: <previous hash block>
        #return: <dict> New block 

        block = {
                'index': len(self.chain)+1,
                'timestamp': time(),
                'transaction': self.carrent_transaction,
                'proof': proof,
                'previous_hash': previous_hash or self.hash(self.chain[-1]),
                }


        #reload 
        self.carrent_transaction = []
        self.chain.append(block) 
        return block  




    def new_transaction(self, sender, recipient, amount):
        self.current_transaction.append({
            'sender':sender,
            'recipient':recipient,
            'amount' : amount,
            })

        return self.last_block['index'] + 1





    @staticmethod  
    def hash(self):
        #hashing block 
        pass


    @property
    def last_block(self):
        #returning the last block of chain
        return self.chain[-1]

