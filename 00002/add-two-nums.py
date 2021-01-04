from __future__ import annotations

from typing import List, Iterator


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def make_list_node(nums: List[int]) -> ListNode:
    root = ListNode(nums[0], None)
    prev = root
    for n in nums[1:]:
        curr = ListNode(n, None)
        prev.next = curr
        prev = curr
    return root


def get_next(l1: ListNode, l2: ListNode) -> Iterator[int]:
    x1 = l1.val
    x2 = l2.val
    c = 0
    while True:
        s = x1 + x2 + c
        c = s // 10
        yield int(s % 10)

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
        x1 = 0 if l1 is None else l1.val
        x2 = 0 if l2 is None else l2.val

        if l1 is None and l2 is None:
            break
    if c > 0:
        yield c


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = []
        res_digits = get_next(l1, l2)
        for r in res_digits:
            result.append(r)
        return result


s = Solution()

assert s.addTwoNumbers(l1=make_list_node([2, 4, 3]), l2=make_list_node([5, 6, 4])) == [
    7,
    0,
    8,
]
assert s.addTwoNumbers(
    l1=make_list_node([9, 9, 9, 9, 9, 9, 9]), l2=make_list_node([9, 9, 9, 9])
) == [8, 9, 9, 9, 0, 0, 0, 1]
assert s.addTwoNumbers(l1=make_list_node([0]), l2=make_list_node([0])) == [0]
