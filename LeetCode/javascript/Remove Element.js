/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    let fixed = nums.filter(a => a !== val);
    
    nums.forEach(function(el, index, array) {
            array[index] = fixed[index];
        });
    
    let dif = nums.length - fixed.length;
    for(let i = 0; i < dif; i++)
    {
        nums.pop()
    }
};