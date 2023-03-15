var minOperations = function(nums) {
    var toRt = 0;

    for (let i = 0; i < nums.length - 1; i++) {
        const el = nums[i];
        const ne = nums[i + 1];
        
        if(el >= ne) 
        {
            let dif = el - ne + 1;
            nums[i + 1] = ne + dif;
            toRt += dif;
        }
    }

    return toRt
};
