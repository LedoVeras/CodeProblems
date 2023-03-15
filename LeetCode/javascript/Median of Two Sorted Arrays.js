var findMedianSortedArrays = function(nums1, nums2) 
{
    let arr = nums1.concat(nums2);   
    arr.sort((a, b) => a - b);
    let middle = arr.length / 2;

    console.log(arr);

    if(arr.length % 2 === 0)
    {
        return((arr[middle - 1] + arr[middle]) / 2);
    }else
    {
        return arr[Math.floor(middle)];
    }
};