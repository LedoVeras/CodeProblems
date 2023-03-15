var mergeTwoLists = function(list1, list2) {

    var test = new ListNode(0, null);
    var tpRt = new ListNode(0, test);
    while(!(list1 == null && list2 == null))
    {
        if(list1 != null && (list2 == null || list1.val <= list2.val))
        {
            test.next = new ListNode(list1.val, null);
            test = test.next
            list1 = list1.next;
            continue;
        }

        if(list2 != null && (list1 == null || list2.val < list1.val))
        {
            test.next = new ListNode(list2.val, null);
            test = test.next
            list2 = list2.next;
        }

        
    }

    tpRt = tpRt.next.next;
    return tpRt;
};