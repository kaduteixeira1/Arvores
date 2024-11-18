from matplotlib import pyplot as plt

class Node:
    def __init__(self, key):
        self.key = key
        self.color = "RED"  #Vermelhos por padrão
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.TNULL = Node(0)
        self.TNULL.color = "BLACK"
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert(self, key):
        node = Node(key)
        node.parent = None
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = "RED"

        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y is None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

        if node.parent is None:
            node.color = "BLACK"
            return

        if node.parent.parent is None:
            return

        self.fix_insert(node)

    def fix_insert(self, k):
        while k.parent.color == "RED":
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left  # Tio do nó
                if u.color == "RED":
                    u.color = "BLACK"
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right  # Tio do nó
                if u.color == "RED":
                    u.color = "BLACK"
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = "BLACK"

    def remove(self, key):
        def transplant(u, v):
            if u.parent is None:
                self.root = v
            elif u == u.parent.left:
                u.parent.left = v
            else:
                u.parent.right = v
            v.parent = u.parent

        def minimum(node):
            while node.left != self.TNULL:
                node = node.left
            return node

        z = self.search_tree(self.root, key)
        if z == self.TNULL:
            print(f"Nó com chave {key} não encontrado.")
            return

        y = z
        y_original_color = y.color
        if z.left == self.TNULL:
            x = z.right
            transplant(z, z.right)
        elif z.right == self.TNULL:
            x = z.left
            transplant(z, z.left)
        else:
            y = minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color

        if y_original_color == "BLACK":
            self.fix_delete(x)

    def fix_delete(self, x):
        while x != self.root and x.color == "BLACK":
            if x == x.parent.left:
                s = x.parent.right
                if s.color == "RED":
                    s.color = "BLACK"
                    x.parent.color = "RED"
                    self.left_rotate(x.parent)
                    s = x.parent.right

                if s.left.color == "BLACK" and s.right.color == "BLACK":
                    s.color = "RED"
                    x = x.parent
                else:
                    if s.right.color == "BLACK":
                        s.left.color = "BLACK"
                        s.color = "RED"
                        self.right_rotate(s)
                        s = x.parent.right

                    s.color = x.parent.color
                    x.parent.color = "BLACK"
                    s.right.color = "BLACK"
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == "RED":
                    s.color = "BLACK"
                    x.parent.color = "RED"
                    self.right_rotate(x.parent)
                    s = x.parent.left

                if s.right.color == "BLACK" and s.left.color == "BLACK":
                    s.color = "RED"
                    x = x.parent
                else:
                    if s.left.color == "BLACK":
                        s.right.color = "BLACK"
                        s.color = "RED"
                        self.left_rotate(s)
                        s = x.parent.left

                    s.color = x.parent.color
                    x.parent.color = "BLACK"
                    s.left.color = "BLACK"
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = "BLACK"

    def search_tree(self, node, key):
        if node == self.TNULL or key == node.key:
            return node

        if key < node.key:
            return self.search_tree(node.left, key)
        return self.search_tree(node.right, key)

    # Função para desenhar a árvore
    def draw_tree(self, node, x=0, y=0, level_gap=1, node_gap=1, ax=None, level=1, positions=None):
        if ax is None:
            fig, ax = plt.subplots(figsize=(12, 8))
            positions = {}

        if node != self.TNULL:
            # Define a posição do nó atual
            positions[node.key] = (x, y)
            ax.scatter(x, y, s=300, color="red" if node.color == "RED" else "black")
            ax.text(x, y, str(node.key), color="white" if node.color == "BLACK" else "black", ha="center", va="center")

            # Desenha as conexões
            if node.left != self.TNULL:
                ax.plot([x, x - node_gap / level], [y, y - level_gap], 'k-')
                self.draw_tree(node.left, x - node_gap / level, y - level_gap, level_gap, node_gap, ax, level + 1, positions)

            if node.right != self.TNULL:
                ax.plot([x, x + node_gap / level], [y, y - level_gap], 'k-')
                self.draw_tree(node.right, x + node_gap / level, y - level_gap, level_gap, node_gap, ax, level + 1, positions)

        if ax:
            ax.axis("off")
            return ax

def main():
    rbt = RedBlackTree()

    numbers = [63, 12, 89, 34, 58, 25, 3, 76, 47, 8, 91, 21, 65, 52, 27, 40, 54, 17, 33, 11, 90, 73, 50]

    for num in numbers:
        rbt.insert(num)

    rbt.draw_tree(rbt.root)
    plt.title("Árvore Red-Black")
    plt.show()
    
    rbt.insert(10)
    rbt.draw_tree(rbt.root)
    plt.title("Árvore Red-Black Após Inserção")
    plt.show()
    
    rbt.remove(25)
    rbt.draw_tree(rbt.root)
    plt.title("Árvore Red-Black Após Remoção")
    plt.show()

if __name__ == "__main__":
    main()
