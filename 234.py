class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        first = head
        second = self.reverse(slow)
        
        while first and second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
            
        return True
    
    def reverse(self, node):
        prev = None
        curr = node
        
        while curr:
            _next = curr.next
            curr.next = prev
            prev = curr
            curr = _next
            
        return prev