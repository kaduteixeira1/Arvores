from matplotlib import pyplot as plt

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_left(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def rotate_right(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def insert(self, root, key):
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)
        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)
        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def get_min_value_node(self, node):
        while node.left:
            node = node.left
        return node

    def delete(self, root, key):
        if not root:
            return root
        elif key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            temp = self.get_min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        if not root:
            return root

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.rotate_right(root)
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.rotate_left(root)
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.rotate_right(root)
            return self.rotate_left(root)

        return root

#Função para desenhar a árvore
def draw_tree(node, x=0, y=0, level_gap=1, node_gap=1, ax=None, level=1, positions=None):
    if ax is None:
        fig, ax = plt.subplots(figsize=(12, 8))
        positions = {}
    
    # Adiciona a posição atual
    if node:
        positions[node.key] = (x, y)
        ax.scatter(x, y, s=300, color="lightblue")
        ax.text(x, y, str(node.key), color="black", ha="center", va="center")
        
        # Desenha as conexões
        if node.left:
            ax.plot([x, x - node_gap / level], [y, y - level_gap], 'k-')
            draw_tree(node.left, x - node_gap / level, y - level_gap, level_gap, node_gap, ax, level + 1, positions)
        
        if node.right:
            ax.plot([x, x + node_gap / level], [y, y - level_gap], 'k-')
            draw_tree(node.right, x + node_gap / level, y - level_gap, level_gap, node_gap, ax, level + 1, positions)

    if ax:
        ax.axis("off")
        return ax
    
def main():
    numbers = [63, 12, 89, 34, 58, 25, 3, 76, 47, 8, 91, 21, 65, 52, 27, 40, 54, 17, 33, 11, 90, 73, 50]

    avl_tree = AVLTree()
    avl_root = None

    for num in numbers:
        avl_root = avl_tree.insert(avl_root, num)

    draw_tree(avl_root)
    plt.title("Árvore AVL após inserções")
    plt.show()

    avl_root = avl_tree.insert(avl_root, 10)
    draw_tree(avl_root)
    plt.title("Árvore AVL após inserir 10")
    plt.show()
    
    avl_root = avl_tree.delete(avl_root, 63)
    draw_tree(avl_root)
    plt.title("Árvore AVL após remover 25")
    plt.show()
    
if __name__ == "__main__":
    main()
