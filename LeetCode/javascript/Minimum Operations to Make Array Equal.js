/**
 * @param {number} n
 * @return {number}
 */
var minOperations = function(n) {
    if([1,2].includes(n)){return n === 1? 0 : 1;}

    //[1, 3, 5]
    let toreturn = n % 2 === 0? 1 : 0;    
    let midPosition = (n / 2)- 0.5;

    let middle = (2 * midPosition) + 1;
    
    let start = midPosition % 1 === 0 ? 2 : 3;
    let end = middle - 1;

    let times = Math.floor(midPosition);

    toreturn += (times * (end + start)) / 2;
    return toreturn;
};