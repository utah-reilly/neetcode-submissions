# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1

        if list1.val < list2.val:
            tmp = ListNode(list1.val)
            list1 = list1.next
        else:
            tmp = ListNode(list2.val)
            list2 = list2.next
        head = tmp
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                tmp.next = ListNode(list1.val)
                list1 = list1.next
            else:
                tmp.next = ListNode(list2.val)
                list2 = list2.next
            tmp = tmp.next

        while list1 != None:
            tmp.next = ListNode(list1.val)
            tmp = tmp.next
            list1 = list1.next
        while list2 != None:
            tmp.next = ListNode(list2.val)
            tmp = tmp.next
            list2 = list2.next
        return head





