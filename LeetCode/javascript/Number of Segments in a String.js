/**
 * @param {string} s
 * @return {number}
 */
var countSegments = function(s) {
    if(s === "" || s === undefined || s === null || s.replace(/ /g, '') === ""){return 0}
    while(s.includes("  "))
    {
        s = s.replace("  ", " ")
    }

    return s.trim().split(" ").length;
};
