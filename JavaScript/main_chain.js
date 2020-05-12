class Block{
    constructor(index,timestamp,data,previousHash=''){
        this.index = index;
        this.timestamp = timestamp;
        this.data = data;
        this.previousHash = previousHash;
        this.hash = this.calculateHash();
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
        var data = this.index + this.timestamp + this.previousHash + JSON.stringify(this.data);
        var hash = get_sha1(data);
        return hash;
    }
}


class Blockchain{
    constructor(){
        this.chain = [this.createGenesisBlock()];
    }
    
    createGenesisBlock(){
        return new Block(0,"2019/03/07","Genesis Block","0000");  
    }

    getLatestBlock(){
        return this.chain[this.chain.length - 1];
    }

    addBlock(newBlock){
        newBlock.previousHash = this.getLatestBlock().hash;
        newBlock.hash = newBlock.calculateHash();
        this.chain.push(newBlock); 
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
Ayumu.addBlock(new Block(1,"2019/03/08","Second Block"));
Ayumu.addBlock(new Block(2,"2019/03/09","Third Block"));

console.log(Ayumu)
