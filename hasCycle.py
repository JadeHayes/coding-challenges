from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = [head]

        node = head
        while node.next:
            if node.next in seen:
                return True
            if node not in seen:
                seen.append(node)
            node = node.next
        return False
                