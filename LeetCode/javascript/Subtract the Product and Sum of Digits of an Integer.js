var subtractProductAndSum = function(n) {
    let arr = n.toString().split("").map(a => parseInt(a));
    return arr.reduce(((a, b) => a * b) , 1) - arr.reduce(((a, b) => a + b) , 0);
};