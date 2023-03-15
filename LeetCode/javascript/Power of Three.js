/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfThree = function(n) {
    if(!(n > 0)){return false}
    var res = Math.log(n) / Math.log(3);
    
    return Number.isInteger(res) || res.toString().includes("0000000000");
};
