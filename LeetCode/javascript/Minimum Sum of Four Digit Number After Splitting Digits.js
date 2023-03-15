var minimumSum = function(num) {
  
    let arr = num.toString().split("").sort((a , b) => a - b);

    return parseInt(arr[0] + arr[3]) + parseInt(arr[1] + arr[2]);
};
