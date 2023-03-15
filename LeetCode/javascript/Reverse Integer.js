/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    let sign = Math.sign(x);
    let cur = x.toString().split("").reverse().join("");
    let int = parseInt(cur)
    if(int < -Math.pow(2, 31) || int > Math.pow(2,31) - 1) {return 0;}
    return int * sign;
};