var convertToTitle = function(columnNumber) {
    
    const alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'];

    let curDiv = 1;
    let next = 1;
    let toRt = "";
    let fst = true;

    while(Math.max(2, columnNumber)  >= next) 
    {
        let curCollum = (Math.floor((columnNumber - (fst? 0 : 1)) / curDiv) - 1) % 26;
        toRt += alphabet[curCollum];

        curDiv *= 26;
        next *= 26;
        next ++;
        fst = false;
    }

    return toRt.split("").reverse().join("");
};