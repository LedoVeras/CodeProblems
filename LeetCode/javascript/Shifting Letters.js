var shiftingLetters = function(s, shifts) 
{
    const alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'];

    let toRt = [];
    let curSum = 0;
    for(let i = s.length - 1; i >= 0; i--)
    {
        curSum += shifts[i];
        
        toRt.unshift(alphabet[(curSum + alphabet.indexOf(s[i])) % 26]);
    }

    return toRt.join("");
};
