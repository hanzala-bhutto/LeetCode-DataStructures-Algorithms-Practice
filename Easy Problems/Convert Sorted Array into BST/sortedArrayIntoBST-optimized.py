# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def insertMidRecursive(self,nums,low,high):
        if (low>high):
            return None
        mid = (low+high)//2
        root = TreeNode(nums[mid])
        root.left=self.insertMidRecursive(nums,low,mid-1)
        root.right=self.insertMidRecursive(nums,mid+1,high)

        return root


    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        return self.insertMidRecursive(nums,0,len(nums)-1)