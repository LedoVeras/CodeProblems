var sortString = function(a)
{
    return a.split("").sort().join("");
}

var groupAnagrams = function(strs) {

    let strSorted = strs.map(sortString);
    let noRpt = [...new Set(strSorted)];
    let toReturn = [];

    for (let j = 0; j < noRpt.length; j++) {
        toReturn.push([]);
    }
    
    for(let i = 0; i < strs.length; i++) 
    {
        toReturn[noRpt.indexOf(strSorted[i])].push(strs[i]);
    }   

    return toReturn;
};