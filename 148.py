	class Solution(object):
		def sortList(self, head):
			"""
			:type head: ListNode
			:rtype: ListNode
			"""
			if not head or not head.next:
				return head
			fast  = head
			slow = head
			while fast.next and fast.next.next:
				slow = slow.next
				fast = fast.next.next
			right = self.sortList(slow.next)
			slow.next = None
			left = self.sortList(head)
			dummy = start = ListNode(0)
			while left and right:
				if left.val <= right.val:
					start.next = left
					left = left.next
				else:
					start.next = right
					right = right.next
				start = start.next
			while left:
				start.next = left
				left = left.next
				start = start.next
			while right:
				start.next = right
				right = right.next
				start = start.next
			return dummy.next