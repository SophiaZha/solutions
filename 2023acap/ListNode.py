class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def find_middle(head):
    if not head:
        return None

    slow_ptr = head
    fast_ptr = head

    while fast_ptr is not None and fast_ptr.next is not None:
        slow_ptr = slow_ptr.next  # Move the slow pointer one step
        fast_ptr = fast_ptr.next.next  # Move the fast pointer two steps

    return slow_ptr.value

# Example usage:
# Create a sample linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

middle_element = find_middle(head)
print(f"The middle element is: {middle_element}")
