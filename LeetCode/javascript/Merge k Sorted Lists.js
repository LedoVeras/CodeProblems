/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode[]} lists
 * @return {ListNode}
 */
var mergeKLists = function(lists) {
    var test = new ListNode(0, null);
    var tpRt = new ListNode(0, test);

    let idx = 0;
    min = 10001
    while(true)
    {   
        min = 10001;

        for(let i = 0; i < lists.length; i++)
        {
            let cur = lists[i];
            if(cur == null){continue;}

            if(cur.val <= min)
            {
                min = cur.val
                idx = i;
            }
        }
        let cur = lists[idx];
        
        if(cur != null){
            test.next = new ListNode(cur.val, null);
            test = test.next
            lists[idx] = cur.next;
        }

        if(lists.every(a => a == null)) {break;};
    }

    return tpRt.next.next;
};

