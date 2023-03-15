/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) 
{
    s = s.trim().split("").reverse().join("") + " ";
    return s.indexOf(" ");
};