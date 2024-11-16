# Reverse Linked List
# Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

# Example 1:
# Input: head = [0,1,2,3]
# Output: [3,2,1,0]

# Example 2:
# Input: head = []
# Output: []

# Constraints:
# 0 <= The length of the list <= 1000.
# -1000 <= Node.val <= 1000

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

res = Solution()
print(linked_list_to_list(res.reverseList(list_to_linked_list([0,1,2,3]))))