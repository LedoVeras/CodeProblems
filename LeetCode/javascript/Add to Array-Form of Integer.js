var addToArrayForm = function(num, k) {

    let kArr = k.toString().split("").map(a => parseInt(a));

    while(num.length < kArr.length) 
        num.unshift(0);

    for (let i = num.length - 1, j = kArr.length - 1; j >= 0; i--, j--) 
    {
        num[i] += kArr[j];
    }
    
    delete kArr;

    for (let i = num.length - 1; i >= 0; i--) 
    {
        if(num[i] >= 10)
        {
            num[i] -= 10;

            if(i === 0)
                num.unshift(1);
            else
                num[i - 1] ++;
        }
    }
      
    return num;
};