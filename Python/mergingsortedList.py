 def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sortedlist = temp = ListNode()
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                temp.next = ListNode(list1.val)
                temp = temp.next
                list1 = list1.next
            else:
                temp.next = ListNode(list2.val)
                temp = temp.next
                list2 = list2.next
        if list1 == None:
            while list2 != None:
                temp.next = ListNode(list2.val)
                temp = temp.next
                list2 = list2.next
        else:
            while list1 != None:
                temp.next = ListNode(list1.val)
                temp = temp.next
                list1 = list1.next
        return sortedlist.next