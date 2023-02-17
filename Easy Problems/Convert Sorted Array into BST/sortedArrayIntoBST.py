# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def insertNode(self,treeNode,x):

        node=treeNode
        parent=None
        while(node):
            parent=node
            if (x>node.val):
                node=node.right
            else:
                node=node.left
        
        if(x>parent.val):
            parent.right=TreeNode(x)
        else:
            parent.left=TreeNode(x)

    def insertRecursive(self,node,nums,low,high):
        if(low<=high):
            mid = ceil((low+high)/2)
            if mid!=len(nums)//2:
                self.insertNode(node,nums[mid])

            self.insertRecursive(node,nums,low,mid-1)
            self.insertRecursive(node,nums,mid+1,high)


    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        if len(nums)==0:
            return 0

            
        node = TreeNode(nums[len(nums)//2])
        
        self.insertRecursive(node,nums,0,len(nums)-1)
        return node
    
