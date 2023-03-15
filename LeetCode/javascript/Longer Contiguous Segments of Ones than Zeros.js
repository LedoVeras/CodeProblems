var checkZeroOnes = function(s) 
{
    let maxct1 = 0,
    maxct0 = 0;
    
    let cur1 = 0,
    cur0 = 0;
    
    for (let i = 0; i < s.length; i++) {
        let el = s[i];
        
        if(el == 1)
        {
            cur1 ++;
            maxct0 = Math.max(maxct0, cur0);
            cur0 = 0;
        }else{
            cur0 ++;
            maxct1 = Math.max(maxct1, cur1);
            cur1 = 0;
        }

        if(i == s.length - 1){maxct0 = Math.max(maxct0, cur0);maxct1 = Math.max(maxct1, cur1);}
    }

    return maxct1 > maxct0;
};