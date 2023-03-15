/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfTwo = function(n) {
    if(!(n > 0)){return false}
    var res = Math.log(n) / Math.log(2);

    return Number.isInteger(res) || res.toString().includes("000000000000");
};