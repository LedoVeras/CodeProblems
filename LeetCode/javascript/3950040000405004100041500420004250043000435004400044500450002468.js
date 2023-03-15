/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    
    for (let i = 0; i < nums.length; i++) {
        let el = nums[i];
        
        let idx = nums.findIndex((a, idx) => idx != i && a == target - el);
        if(idx != -1){
            return [i, idx];
        }
    }
};