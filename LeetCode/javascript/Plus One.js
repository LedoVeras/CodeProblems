var plusOne = function(digits) {
    
    for (let i = digits.length - 1; i >= 0; i--) {
        
        if(i === digits.length - 1)
            digits[i] ++;
        
        const element = digits[i];

        if(element >= 10)
        {
            digits[i] = 0;
            
            if(i === 0)
                digits.unshift(1);
            else
                digits[i - 1] ++;
        }
    }  
    return digits;
};