/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) 
{
    let prev = 0;
    let toRt = 1;

    for(let i = 0; i < n; i++)
    {
        toRt += prev;
        prev = toRt - prev;
    }

    return toRt;
};