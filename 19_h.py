# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head.next and n == 1:
            return head.next
                
        len_head, j = 0, 0   
        temp1 = temp2 = head
        
        while temp1:
            len_head += 1
            temp1 = temp1.next
            
        while temp2:
            if len_head == n:
                return head.next
            
            j += 1
            if j == len_head-n:
                temp3 = temp2
                temp2 = temp2.next
                temp2 = temp2.next
                temp3.next = temp2
                break
            temp2 = temp2.next
                              
        return head
            
            