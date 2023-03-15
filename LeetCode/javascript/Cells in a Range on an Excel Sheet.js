cellsInRange = function(s) {
    const alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'];
    const letters = [s[0], s[3]];    
    const numbers = [parseInt(s[1]) , parseInt(s[4])];

    let returnArr = [];

    for (let i = alphabet.indexOf(letters[0]); i <= alphabet.indexOf(letters[1]); i++) 
    {
        for (let j = numbers[0]; j <= numbers[1]; j++) 
        {         
            returnArr.push(alphabet[i] + j.toString());
        }
    }

    return returnArr;
};
