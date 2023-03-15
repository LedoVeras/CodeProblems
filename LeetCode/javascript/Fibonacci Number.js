/**
 * @param {number} n
 * @return {number}
 */
var fib = function(n) {
    if(n <= 1){return [0, 1][n]}
    let prev = 0;
    let toRt = 1;

    for(let i = 0; i < n - 1; i++)
    {
        toRt += prev;
        prev = toRt - prev;
    }

    return toRt;
};