const possible = ["()", "[]", "{}"];

var isValid = function(s) {
    if(s.length === 1) {return false;}

    while(s.includes(possible[0]) || s.includes(possible[1]) || s.includes(possible[2])) 
        for(let i = 0; i < 3; i++)
            s = s.replaceAll(possible[i], "");
    
    return s === "";
};