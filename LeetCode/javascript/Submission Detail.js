var titleToNumber = function(columnTitle)
{
    const alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'];
    let sum = 0;

    for (let i = columnTitle.length - 1, j = 0; i >= 0; i--, j++) 
    {
        const element = columnTitle[i];

        sum += (alphabet.indexOf(element) + 1) * (26 ** j);
    }

    return sum;
};
