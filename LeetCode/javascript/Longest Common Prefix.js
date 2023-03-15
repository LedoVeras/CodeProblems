var longestCommonPrefix = function(strs) 
{
    let cmPre = "";

    let stop = false;

    while(true)
    {
        strs.forEach(a => 
            {
                if((a.slice(0, cmPre.length) !== cmPre && cmPre !== "") || a === "")
                {
                    stop = true;
                    cmPre = cmPre.slice(0, -1);
                }
            })
        
        let add = strs[0][cmPre.length];

        if(stop || add === undefined) {break;}
        
        cmPre += add;
    }
    
    return cmPre;
};