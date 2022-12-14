# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = temp = ListNode(0)
        
        while list1 and list2: 
            
            if list2.val < list1.val:
                temp.next = list2
                list2 = list2.next
                
            else:
                temp.next = list1
                list1 = list1.next 
                
            temp = temp.next           
        temp.next = list1 or list2
        
        return head.next
    
  