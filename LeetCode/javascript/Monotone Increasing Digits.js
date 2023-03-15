var monotoneIncreasingDigits = function(n) 
{
    let nu = n.toString().split("").map(a => parseInt(a));

    for(let i = nu.length - 1; i > 0; i--)
    {
        let ne = nu[i - 1];

        if(ne > nu[i]){
            nu[i] = 9;
            nu[i - 1] --;

            for(let j = nu.length - 1; j > i; j--){
                nu[j] = 9;
            }
        }
    }

    return nu.filter((a) => a !== 0).join("");
};