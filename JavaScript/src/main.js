const {Blockchain, Transaction} = require("./blockchain");
const EC = require("elliptic").ec;
const ec = new EC("secp256k1");

const myKey = ec.keyFromPrivate("0ace40a0be404be501cf0658dc63bcd6d4b844aa8bb5b3a0b30c5c05ad03a213");
const myWalletAddress = myKey.getPublic("hex");

let Ayumu = new Blockchain();

const tx1 = new Transaction(myWalletAddress,"public key goes here",10)
tx1.signTransaction(myKey);
Ayumu.addTransaction(tx1);

console.log("\n starting miner...");
Ayumu.minePendingTransactions(myWalletAddress);

console.log("\n Balance of xayumu: ",Ayumu.getBalanceOfAddress(myWalletAddress));

