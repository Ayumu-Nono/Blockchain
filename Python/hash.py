from blockchain import Blockchain #クラスの読み込み
import json #データ形式の指定
import hashlib #ハッシュのクラスを読み込む


def calculate_hash(block):#blockという引数に対してハッシュ関数を作る 
    block_string = json.dumps(block).encode()#文字変換
    return hashlib.sha256(block_string).hexdigest()#ハッシュ関数

blockchain = Blockchain()
# blockにはジェネシスブロック
block = blockchain.chain[0]#Blockcainクラスのchain配列の1番目の箱
hash_value = calculate_hash(block)

print(hash_value)#ジェネシスブロックのハッシュ値