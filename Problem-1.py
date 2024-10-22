'''
    Time Complexity: O(n)
    Space Complexity: O(n/2)
    Approach: BFS - Level order traversal
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        queue = deque()

        if not root:
            return result

        queue.append(root)
        size = len(queue)

        while len(queue):
            level = []
            for i in range(size):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(level)
            size = len(queue)

        return result
        