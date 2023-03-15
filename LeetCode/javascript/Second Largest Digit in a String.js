var secondHighest = function(str) {
    let numbers = str.match(/[0-9]+/g);
    if(numbers == null) {return -1;}
    let noRpt = [...new Set(  numbers.join('').split('')  )].sort((a, b) => b - a);
    return parseInt(noRpt.length > 1? noRpt[1] : -1);
};
