from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def reverseListGood(self, head: [ListNode]) -> [ListNode]:
        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev

    def reverseListRecursive(self, head: ListNode) -> ListNode:
        print("calling reverse: " + str(None if head == None else head.val))
        if not head:
            return None
        newHead = head
        if head.next:
            newHead = self.reverseListRecursive(head.next)
            head.next.next = head
        head.next = None

        print("ending  reverse: " + str(newHead.val))
        return newHead

    def reverseListR(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return p

    def to_linked_list(self,iterable):
        head = None
        for val in reversed(iterable):
            head = ListNode(val, head)
        return head

    def to_native_list(self,head):
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        return lst

sol = Solution()
result = sol.to_linked_list([1,2,3,4,5])
reversedList = sol.reverseList(result)
reversedList = sol.reverseListRecursive(result)
print(sol.to_native_list(reversedList))

result = sol.to_linked_list([])
reversedList = sol.reverseListRecursive(result)
print(sol.to_native_list(reversedList))

result = sol.to_linked_list([1,2])
reversedList = sol.reverseListRecursive(result)
print(sol.to_native_list(reversedList))

"""
206. Reverse Linked List
Easy

14274

247

Add to List

Share
Given the head of a singly linked list, reverse the list, and return the reversed list.



Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []


Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000


Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

Accepted
2,476,609
Submissions
3,447,006
"""