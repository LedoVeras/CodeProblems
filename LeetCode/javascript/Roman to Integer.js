const RomanInteger = 
      {
          IV:4,
          IX:9,
          XL:40,
          XC:90,
          CD:400,
          CM:900,
          I:1,
          V:5,
          X:10,
          L:50,
          C:100,
          D:500,
          M:1000
      }

var romanToInt = function(s) {
    
    let sUp = s.toUpperCase();
    let result = 0;
    
    for (let i = 0; i < s.length; i++) 
    {
        let curStr = sUp.slice(i , i + 2);
        let curInt = 0;

        if(curStr.length > 1 && RomanInteger[curStr] !== undefined)
        {
            curInt = RomanInteger[curStr];
            i++
        }else{
            curInt = RomanInteger[s[i]];
        }

        result += curInt;
    }

    return result;
};