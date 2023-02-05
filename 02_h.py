# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        d1, d2 = 0, 0
        num1 , num2 = 0, 0
        head = temp = ListNode(0)
        
        while l1:
            num1 += l1.val * (10 ** d1)
            l1 = l1.next
            d1 += 1
        
        while l2:
            num2 += l2.val * (10 ** d2)
            l2 = l2.next
            d2 +=1
            
        sun = num1 + num2
        s_sun = str(sun)
        
        for i in reversed(range(len(s_sun))):        
            temp.next = ListNode(s_sun[i])
            temp = temp.next
            
        return head.next
        
       