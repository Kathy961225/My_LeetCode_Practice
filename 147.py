Given 1 -> 3 -> 2 -> 4 - > null

dummy0 -> 1 -> 3 -> 2 -> 4 - > null
               |    |
              ptr toInsert
-- locate ptr = 3 by (ptr.val > ptr.next.val)
-- locate toInsert = ptr.next

dummy0 -> 1 -> 3 -> 2 -> 4 - > null
          |         |
   toInsertPre     toInsert
-- locate preInsert = 1 by preInsert.next.val > toInsert.val
-- insert toInsert between preInsert and preInsert.next



def insertionSortList(self, head):

        dummyHead = ListNode(0)
        dummyHead.next = nodeToInsert = head
        
        while head and head.next:
            if head.val > head.next.val:
                # Locate nodeToInsert.
                nodeToInsert = head.next
                # Locate nodeToInsertPre.
                nodeToInsertPre = dummyHead
                while nodeToInsertPre.next.val < nodeToInsert.val:
                    nodeToInsertPre = nodeToInsertPre.next
                    
                head.next = nodeToInsert.next
                # Insert nodeToInsert between nodeToInsertPre and nodeToInsertPre.next.
                nodeToInsert.next = nodeToInsertPre.next
                nodeToInsertPre.next = nodeToInsert
            else:
                head = head.next
            
        return dummyHead.next