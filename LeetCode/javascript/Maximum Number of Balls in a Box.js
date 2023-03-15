var countBalls = function(lowLimit, highLimit) 
{   
    let st = performance.now();
    let n = highLimit - lowLimit + 1;
    let boxes = new Array(46).fill(0);

    for(let i = lowLimit; i <= highLimit; i++)
    {
        boxes[sunAlgorithm(i)] ++;
    }

    return boxes.sort((a, b) => b - a)[0];
};

var sunAlgorithm = function(int)
{
    return int.toString().split("").reduce(sumStr);
}

var sumStr = function(a, b)
{
    return parseInt(a) + parseInt(b);
}
