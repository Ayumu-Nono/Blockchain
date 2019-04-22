class Transaction{
    constructor(fromAddress,toAddress,amount){
        this.fromAddress = fromAddress;
        this.toAddress = toAddress;
        this.amount = amount;
    }
}

class Block{
    constructor(timestamp,transactions,previousHash=''){
        this.timestamp = timestamp;
        this.transactions = transactions;
        this.previousHash = previousHash;
        this.hash = this.calculateHash();
        this.nonce = 0;
    }

    calculateHash(){
        function get_hash(algorithm, plaintext, encoding) {
            var crypto = require('crypto');
            var hashsum = crypto.createHash(algorithm);
            hashsum.update(plaintext);
            return hashsum.digest(encoding);
        }       
        function get_sha1(plaintext) {
        return get_hash('sha1', plaintext, 'hex');
        }
        var data = (this.index + this.timestamp + this.previousHash + this.nonce + JSON.stringify(this.transactions)).toString();
        var hash = get_sha1(data);
        return hash;
    }

    mineBlock(difficulty){
        while(this.hash.substring(0,difficulty) !== Array(difficulty+1).join("0")){
            this.nonce++;

            this.hash = this.calculateHash(); 
        }
        console.log("Block mined: "+ this.hash);

    }
}


class Blockchain{
    constructor(){
        this.chain = [this.createGenesisBlock()];
        this.difficulty = 2;
        this.pendingTransactions = [];
        this.miningReward = 100; 
    }
    
    createGenesisBlock(){
        return new Block("2019/03/07","Genesis Block","0000");  
    }

    getLatestBlock(){
        return this.chain[this.chain.length - 1];
    }

    minePendingTransactions(miningRewardAddress){
        let block = new Block(Date.now(),this.pendingTransactions);
        block.mineBlock(this.difficulty);

        console.log("Block successfully mined!");
        this.chain.push(block);

        this.pendingTransactions = [
            new Transaction(null,miningRewardAddress,this.miningReward)
        ];
    }

    createTransaction(transaction){
        this.pendingTransactions.push(transaction);
    }

    getBalanceOfAddress(address){
        let balance = 0;

        for(const block of this.chain){
            for(const trans of block.transactions){
                if(trans.fromAddress === address){
                    balance -= trans.amount;
                }
                if(trans.toAddress === address){
                    balance += trans.amount;
                }
            }
        }
        return balance;
    }

    isChainValid(){
        for(let i=1;i<this.chain.length;i++){
            const currentBlock = this.chain[i];
            const previousBlock = this.chain[i-1];
            if(currentBlock.hash !== currentBlock.calculateHash()){
                return false;
            }
            if(currentBlock.previousHash !== previousBlock.hash){
                return false;
            }
        }

        true;
    }
}

let Ayumu = new Blockchain();
Ayumu.createTransaction(new Transaction("address1","address2",100));
Ayumu.createTransaction(new Transaction("address2","address1",50));

console.log("\n starting miner...");
Ayumu.minePendingTransactions("xayumu-address");

console.log("\n Balance of xayumu: ",Ayumu.getBalanceOfAddress("xayumu-address"));

console.log("\n starting miner...");
Ayumu.minePendingTransactions("xayumu-address");

console.log("\n Balance of xayumu: ",Ayumu.getBalanceOfAddress("xayumu-address"));
