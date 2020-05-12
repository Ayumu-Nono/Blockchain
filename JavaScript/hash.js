function get_hash(algorithm, plaintext, encoding) {
    var crypto = require('crypto');
    var hashsum = crypto.createHash(algorithm);
    hashsum.update(plaintext);
    return hashsum.digest(encoding);
}       
function get_sha1(plaintext) {
return get_hash('sha1', plaintext, 'hex');
}
var data = 'hoge';
var hash = get_sha1(data);
console.log(hash);