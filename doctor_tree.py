class DoctorNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class DoctorTree:
    def __init__(self):
        self.root = None

    def insert(self, parent_name, employee_name, side, current_node=None):
        # Reject invalid sides before searching
        if side not in ("left", "right"):
            print("Side must be 'left' or 'right'.")
            return False

        if self.root is None:
            print("Tree is empty. Set the root doctor first.")
            return False

        # Track the original call so a missing parent is reported only once
        first_call = current_node is None

        if current_node is None:
            current_node = self.root

        # Attach the new doctor when the parent is found
        if current_node.name == parent_name:
            if side == "left":
                if current_node.left is not None:
                    print("Left report already exists.")
                    return False
                current_node.left = DoctorNode(employee_name)
            else:
                if current_node.right is not None:
                    print("Right report already exists.")
                    return False
                current_node.right = DoctorNode(employee_name)

            return True

        # Search the left subtree
        if current_node.left is not None:
            if self.insert(parent_name, employee_name, side, current_node.left):
                return True

        # Search the right subtree
        if current_node.right is not None:
            if self.insert(parent_name, employee_name, side, current_node.right):
                return True

        if first_call:
            print("Parent doctor not found.")

        return False

    def preorder(self, node):
        # Base case, no node at this position
        if node is None: 
            return []

        # Visit current doctor, then left and right subtrees
        result = [node.name]
        result += self.preorder(node.left)
        result += self.preorder(node.right)
        return result

    def inorder(self, node):
        if node is None: 
            return []
 
        # Visit the left subtree, current doctor, then right subtree
        result = []
        result += self.inorder(node.left)
        result.append(node.name)
        result += self.inorder(node.right)
        return result

    def postorder(self, node):
        if node is None:
            return []

        # Visit left and right subtrees, then current doctor
        result = []
        result += self.postorder(node.left)
        result += self.postorder(node.right)
        result.append(node.name)
        return result

# Test your DoctorTree and DoctorNode classes here

tree = DoctorTree()
tree.root = DoctorNode("Dr. Croft") 
# Insert values
tree.insert("Dr. Croft", "Dr. Goldsmith", "right") 
tree.insert("Dr. Croft", "Dr. Phan", "left")
tree.insert("Dr. Phan", "Dr. Carson", "right") 
tree.insert("Dr. Phan", "Dr. Morgan", "left")

print(tree.preorder(tree.root))
print(tree.inorder(tree.root))
print(tree.postorder(tree.root))