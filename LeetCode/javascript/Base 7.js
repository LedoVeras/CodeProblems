var convertToBase7 = function(num) 
{
    let sign = num < 0 ? "-" : "";
    num = Math.abs(num);
    let toRt = "";
    while(num !== 0)
    {
        let rest = num % 7;
        num = Math.floor(num / 7);
        toRt = rest + toRt;
    }

    return sign + (toRt? toRt : "0");
};