class Solution:
    # 这题不给head让你删除某个节点，需求有些不明所以
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
