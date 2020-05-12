from blockchain import Blockchain
from hash import calculate_hash
import hashlib


def proof_of_work(blockchain, previous_hash):
    nonce = 0
    while True:
        block = blockchain.create_block(nonce, previous_hash)
        #ひとつ前のハッシュ値を受け取って、一旦チェーンにつなぐ
        guess_hash = calculate_hash(block)#この段階でのナンス値に対してのハッシュ値

        if guess_hash[:4] == "0000":#予想ハッシュ値の先頭から4つが0ならtrue
            break

        # falseならチェーンを削除する
        blockchain.chain.pop()
        nonce += 1
    return block

blockchain = Blockchain()
# このprevious_hashは適当な値です
block_hash = "e5c87e27a81ee16c491a2ca6fe1eb1310caed25d0fab1ccfa785ffbadafeb96b"
block = proof_of_work(blockchain, block_hash)

print(block)

# このnonceが正しいかどうかを確認します
# 0が先頭に続いていれば正しく計算できているとみなすことができる
print("このブロックのハッシュ値 :", calculate_hash(block))