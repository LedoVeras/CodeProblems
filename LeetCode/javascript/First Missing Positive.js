var firstMissingPositive = function(nums) 
{
    nums = [...new Set(nums.filter(a => a > 0).sort((a, b) => a - b))];
    
    if(nums[0] !== 1){return 1}

    for(let i = 0; i < nums.length; i++)
    {
        if(i === nums.length - 1 || nums[i] + 1 !== nums[i + 1])
        {
            return nums[i] + 1;
        }
    }

};