from typing import Optional

class ListNode:
   def __init__(self, val=0, next=None):
      self.val, self.next = val, next

# 2807m Insert Greatest Common Divisors in Linked List
class Solution2807:
   def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
      if head is None or head.next is None:
         return head
      
      a, b = head.val, head.next.val
      if a > b:
         a, b = b, a
      while b != 0:
         a, b = b, a%b

      head.next = ListNode(a, self.insertGreatestCommonDivisors(head.next))
      return head
