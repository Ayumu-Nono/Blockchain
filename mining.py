from proof_of_work import proof_of_work 
from hash import calculate_hash
import time


class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.transaction_index = 0
        
        self.create_transaction(sender='0', recipient="my_address", amount=1)
        proof_of_work(self, previous_hash="00000")

    def create_block(self, nonce, previous_hash):
        block = {
            'index': len(self.chain),
            'timestamp': time.gmtime(),
            'transactions': self.current_transactions,
            'nonce': nonce,
            'previous_hash': previous_hash,
        }
        self.chain.append(block)
        return block

    def create_transaction(self, sender, recipient, amount):
        self.current_transactions.append({
            'transaction_index': self.transaction_index,#何番目のブロックか
            'sender': sender,#送り主
            'recipient': recipient,#受け取る人
            'amount': amount,#数量
        })
        self.transaction_index += 1
        return self.transaction_index - 1, len(self.chain)


blockchain = Blockchain()


def mine(blockchain):
    #proof_of_workをやって、内容をreturnする

    last_block = blockchain.chain[-1]#チェーンそのもの
    previous_hash = calculate_hash(last_block)#直前のブロックのハッシュ値を計算
    proof_of_work(blockchain, previous_hash)#正しければブロックを追加する

    #箱を更新するために空っぽにする
    blockchain.current_transactions = []
    blockchain.transaction_index = 0

    # current_transactionsにコインベースを追加しています
    blockchain.create_transaction(sender='0', recipient="my_address", amount=1)
    block = blockchain.chain[-1]

    # 新しいブロックの情報をresponseに代入しています
    response = {
        'message': '新しいブロックを採掘しました',
        'index': block['index'],
        'nonce': block['nonce'],
        'previous_hash': block['previous_hash'],
    }
    return response


print(mine(blockchain))