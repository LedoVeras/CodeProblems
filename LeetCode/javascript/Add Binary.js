var addBinary = function(a, b) {

    let rt = "";
    let next = false;
    for(let i = a.length - 1, j = b.length - 1; i >= 0 || j >= 0; i-- , j--)
    {
        let elA = a[i]? parseInt(a[i]) : 0;
        let elB = b[j]? parseInt(b[j]) : 0;
        
        let sum = elA + elB + (next? 1 : 0);
        next = false;

        switch (sum)
        {
            case 0:
                rt += "0";
                break;
            case 1:
                rt += "1";
                break;
            case 2:
                rt += "0";
                next = true;
                break;
            case 3:
                rt += "1";
                next = true;
                break;
        }

        if(next && i <= 0 && j <= 0)
            rt += "1";
    }

    return rt.split("").reverse().join("");
};