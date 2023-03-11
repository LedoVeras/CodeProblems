/**
 * @param {number} n
 * @return {boolean}
 */
var isUgly = function(n) {
    if(n <= 1){return n == 1}

    while(true)
    {
        if(n % 2 == 0) { n /= 2; continue;}
        else if(n % 3 == 0) { n /= 3; continue;}
        else if(n % 5 == 0) { n /= 5; continue;}

        return n == 1;
    }
};