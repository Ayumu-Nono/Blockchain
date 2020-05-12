import time
import json


class Blockchain: #classの名前は大文字で始まる
    def __init__(self): #引数が要らなくてもselfを入れないといけない
                        #__2つで外部の参照を受けないメソッド
        self.chain = [] #chainはブロックのつながったチェーンそのものの配列
        self.current_transactions = [] #取引内容を入れる配列
        self.transaction_index = 0 #通し番号。ジェネシスブロックなので0

        # ジェネシスブロックを作成してください
        self.create_block(nonce="hoge", previous_hash="00000")

    # ジェネシスブロックを作成する関数を完成させてください
    def create_block(self, nonce, previous_hash):#引数の1つめは習慣的にself
        block = {
            'index': len(self.chain),#len関数はlengthを返す
            'timestamp': time.gmtime(),#時間を取得 time()にすればepochからの総経過時間
            'transactions': self.current_transactions,#取引内容
            'nonce': nonce,#ナンス値
            'previous_hash': previous_hash,#ひとつまえのブロックのハッシュ値
        }
        # ブロックの追加をします
        self.chain.append(block)#appendで配列要素を追加
        return block


blockchain = Blockchain()
print(blockchain.chain)