from proof_of_work import proof_of_work
import time


class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.transaction_index = 0
        self.create_transaction(sender='0', recipient="my_address", amount=1)
        proof_of_work(self, previous_hash="00000")
        self.nodes = set()

    def create_block(self, nonce, previous_hash):
        block = {
            'index': len(self.chain),
            'timestamp': time.time(),
            'transactions': self.current_transactions,
            'nonce': nonce,
            'previous_hash': previous_hash,
        }
        self.chain.append(block)
        return block

    def create_transaction(self, sender, recipient, amount):
        self.current_transactions.append({
            'transaction_index': self.transaction_index,
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        self.transaction_index += 1
        return self.transaction_index - 1, len(self.chain)

    def create_node(self, nodes):
        # ノードが存在していない場合はエラーが出るようにしてください
        if nodes is None:
            return "Error : 有効ではないノードです。"

        # ノードを追加してください
        for node in nodes:
            self.nodes.add(node)

        # ノードが追加されたことを出力しています
        response = {
            'message': 'ノードが追加されました。',
            'total_nodes': list(self.nodes)
        }
        return response


blockchain = Blockchain()
nodes = ["http://bitcoin_aidemy_first", "http://bitcoin_aidemy_second"]
message = blockchain.create_node(nodes)

print(message)