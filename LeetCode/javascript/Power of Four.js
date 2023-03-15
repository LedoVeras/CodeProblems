/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfFour = function(n) {
    if(!(n > 0)){return false}
    var res = Math.log(n) / Math.log(4);
    
    return Number.isInteger(res) || res.toString().includes("00000000000000");
};