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

    var ant = head;
    while(cur != null && cur.next != null)
    {
        var ne = cur.next;

        if(cur.val == ne.val){
            var curnex = ne;

            while(curnex != null && cur.val == curnex.val)
                curnex = curnex.next;
            
            ant.next = curnex;
            cur = ant.next;

            continue;
        }

        ant = cur;
        cur = cur.next;
    }

    return head.next;
};