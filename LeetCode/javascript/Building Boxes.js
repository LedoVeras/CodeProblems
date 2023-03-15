/**
 * @param {number} n
 * @return {number}
 */
var minimumBoxes = function(n) {
    
    let num = 1;
    let icn = 3;
    let ic = 3;
    
    while(num + icn <= n)
    {
        num += icn;
        icn += ic;
        ic ++;
    }
    icn -= ic - 1;
    ic = 1;
    
    let dif = n - num;

    while(dif > 0)
    {
        dif -= ic;
        ic++;
        icn++;
    }

    return icn;
};