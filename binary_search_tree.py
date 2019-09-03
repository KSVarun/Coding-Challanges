n = int(input())
arr = list(map(int, input().split()))


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# A utility function to insert a new node with the given key


def insert(root, node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)


BST_dict = {}


def prLevel(root):

    if (not root):
        return
# queue to hold tree node with level
    q = []
# let root node be at level 1
    q.append([root, 1, root.val])
    # print(q[2])
    #BST_dict[q[2]] = 1
    p = []

# Do level Order Traversal of tree
    while (len(q)):
        p = q[0]
        q.pop(0)
       # print(p[1])
        BST_dict[p[2]] = p[1]
        if (p[0].left):
            q.append([p[0].left, p[1] + 1, p[0].left.val])
        if (p[0].right):
            q.append([p[0].right, p[1] + 1, p[0].right.val])


r = Node(arr[0])

for i in range(1, len(arr)):
    insert(r, Node(arr[i]))

prLevel(r)

for i in range(len(arr)):
    print(BST_dict[arr[i]], end=' ')
# def inorder(root):
#     if root:
#         inorder(root.left)
#         print(root.val)
#         inorder(root.right)


# inorder(r)
