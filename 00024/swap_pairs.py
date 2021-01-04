from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def make_linked_list(data: List[int]) -> ListNode:
    root = ListNode(data[0])
    idx = 1
    curr = root
    while idx < len(data):
        node = ListNode(data[idx])
        curr.next = node
        curr = node
        idx += 1
    return root


def tolist(curr: ListNode) -> List[int]:
    data = []
    while curr:
        data.append(curr.val)
        curr = curr.next
    return data


def print_ll(curr: ListNode) -> None:
    while curr:
        print(curr.val, end=", ")
        curr = curr.next
    print()


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        first = head
        second = head
        first = first.next
        while first:
            second.val, first.val = first.val, second.val
            first = first.next
            first = first.next if first else None
            second = second.next
            second = second.next if second else None
        return head


s = Solution()

res = s.swapPairs(make_linked_list([1, 2, 3]))
assert tolist(res) == [2, 1, 3]

res = s.swapPairs(make_linked_list([1, 2, 3, 4]))
assert tolist(res) == [2, 1, 4, 3]

res = s.swapPairs(make_linked_list([1]))
assert tolist(res) == [1]