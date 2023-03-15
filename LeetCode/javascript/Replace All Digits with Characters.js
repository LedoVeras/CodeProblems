var replaceDigits = function(s) {
    const alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'];
    let toRt = s.split("");
    for (let i = 1; i < s.length; i += 2) {
        let sum = Math.min(  parseInt( s[i] ) + alphabet.indexOf( s[i - 1] ), 26);
        toRt[i] = alphabet[sum];
    }
    return toRt.join("");
};