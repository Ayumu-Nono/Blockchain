from proof_of_work import proof_of_work
import time


class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.transaction_index = 0
        self.create_transaction(sender='0', recipient="my_address", amount=1)
        proof_of_work(self, previous_hash = "00000")
        self.nodes = set()

    def create_block(self, nonce, previous_hash):
        block = {
            'index' : len(self.chain),
            'timestamp' : time.time(),
            'transactions' : self.current_transactions,
            'nonce' : nonce,
            'previous_hash' : previous_hash,
        }
        self.chain.append(block)
        return block

    def create_transaction(self, sender, recipient, amount):
        self.current_transactions.append({
            'transaction_index' : self.transaction_index,
            'sender' : sender,
            'recipient' : recipient,
            'amount' : amount,
            })
        self.transaction_index += 1
        # 追加したトランザクションのindexと追加されるブロックを返してください
        return self.transaction_index - 1, len(self.chain)

blockchain = Blockchain()
sender = "ishikawa"
recipient = "kawai"
amount = 5
transaction_num, block_num = blockchain.create_transaction(sender, recipient, amount)
print("追加されたtransaction :", transaction_num)
print("追加されるblock :", block_num)