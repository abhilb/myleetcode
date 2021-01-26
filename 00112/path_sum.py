from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.target_found = False

    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        self.target_found = False
        self.dfs(root, targetSum, 0)
        return self.target_found

    def dfs(self, node: TreeNode, targetSum: int, currentSum: int):
        if node and self.target_found == False:
            currentSum += node.val
            if node.left == None and node.right == None:
                self.target_found = currentSum == targetSum
                return

            self.dfs(node.left, targetSum, currentSum)
            self.dfs(node.right, targetSum, currentSum)


s = Solution()


def insertLevelOrder(arr, root, i):
    if i < len(arr):
        temp = TreeNode(arr[i])
        root = temp
        root.left = insertLevelOrder(arr, root.left, 2 * i + 1)
        root.right = insertLevelOrder(arr, root.right, 2 * i + 2)
    return root


data = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
root = insertLevelOrder(data, None, 0)
print(s.hasPathSum(root, 22))

data = [1, 2, 3]
root = insertLevelOrder(data, None, 0)
print(s.hasPathSum(root, 5))

data = [1, 2]
root = insertLevelOrder(data, None, 0)
print(s.hasPathSum(root, 0))

data = [0, 1, 1]
root = insertLevelOrder(data, None, 0)
print(s.hasPathSum(root, 1))