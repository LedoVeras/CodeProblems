var checkOnesSegment = function(s) {
    for (let i = 1; i < s.length; i++) {
        let el = s[i];
        
        if(el == 1 && s[i - 1] == 0){
            return false;
        }
    }
    return true;
};