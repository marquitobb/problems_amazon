"""Homeinterview prepration kitHackerRank Tree: Height of a Binary Tree problem solution
HackerRank Tree: Height of a Binary Tree problem solution
YASH PALMarch 15, 2021

In this HackerRank Tree: height of a binary tress Interview preparation kit problem you need to complete the getHeight or height function. It must return the height of a binary tree as an integer.

HackerRank Tree: Height of a Binary Tree solution


Problem solution in Python programming."""
from array import array


class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                # print("current: ", current.info)
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        # print("right: ", current.right)
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

def height(root):
    leftHeight = 0
    rightHeight = 0

    if(root.left):
        leftHeight = height(root.left) + 1

    if(root.right):
        rightHeight = height(root.right) + 1

    if(leftHeight > rightHeight):
        return leftHeight
    else:
        return rightHeight

# def levelOrder(root, data=[], level=0):
#     if root:
#         if data == []:
#             data.append(root.info)
#         if root.left:
#             data.append(root.left.info)
#         if root.right:
#             data.append(root.right.info)
#         levelOrder(root.left, data, level+1)
#         levelOrder(root.right, data, level+1)
#     if level == 0:
#         dt = ""
#         for i in data:
#             dt += str(i) + " "
#         print(dt)

def levelOrder(root):
    queue = []
    data = []
    queue.append(root)
    while(len(queue)>0):
        node = queue.pop(0)
        data.append(node.info)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    dt = ""
    for i in data:
        dt += str(i) + " "
    print(dt)



tree = BinarySearchTree()

tree.create(1)
tree.create(2)
tree.create(5)
tree.create(3)
tree.create(6)
tree.create(4)
tree.create(9)
tree.create(7)


print("altura--->",height(tree.root))
levelOrder(tree.root)
# print("levelOrder--->",levelOrder(tree.root))