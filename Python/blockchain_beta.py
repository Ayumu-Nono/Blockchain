# 今までの内容を実装しています
from blockchain import Blockchain
from mining import mine
from transaction import Blockchain
import json
blockchain = Blockchain()
# mine(blockchain)


def create_transactions(blockchain, values):
    required = ["sender", "recipient", "amount"]#要求取引内容
    # allモジュールの中身を作成して要求形式が正しいか見る
    if not all([element in values for element in required]):
        return "valueの形式が正しくありません"

    # それぞれ渡して、新しいトランザクション追加
    transaction_index, block_index = blockchain.create_transaction(
        values["sender"], values["recipient"], values["amount"])

    response = {
        "message": f"トランザクションはブロック {block_index}の {transaction_index}番目 に追加されました"}
    return response




#この先は別ファイルにした方が良いか
values1=json.load(open('data/input.json'))

values=values1
create_transactions(blockchain, values)
print(blockchain.chain[0])

output = open('data/output.json' , 'w')
json.dump(blockchain.chain[0],output)