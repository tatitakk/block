class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transaction = []




    def new_blck(self):
        #creation new block and adding
        pass 






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
        pass

