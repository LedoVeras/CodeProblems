/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var deleteDuplicates = function(head) {
    var cur = head;
    head = new ListNode(0, cur);

    while(cur != null && cur.next != null)
    {
        var ne = cur.next;

        if(cur.val == ne.val){
            cur.next = ne.next
            continue;
        }

        cur = cur.next;
    }
    

    return head.next;
};