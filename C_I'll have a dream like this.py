tree = {}
N, Q = list(map(int, input().split()))
commands = list(map(int, input().split()[:Q]))


def switch(value: int, tree: dict):
    parent = 0
    is_left_child = False
    for p in tree:
        left, right = tree[p]
        if left == value:
            parent = p
            is_left_child = True
            break
        elif right == value:
            parent = p
            is_left_child = False
            break
    
    if parent == 0:
        return
    
    grandparent = 0
    is_parent_left_child = False
    for pp in tree:
        left, right = tree[pp]
        if left == parent:
            grandparent = pp
            is_parent_left_child = True
            break
        elif right == parent:
            grandparent = pp
            is_parent_left_child = False
            break
    
    # Сохраняем детей value и parent (если нет ребенка, будет 0)
    vl, vr = tree.get(value, [0, 0])
    pl, pr = tree.get(parent, [0, 0])
    
    # Обновляем связи в зависимости от того, является ли value левым или правым ребенком
    if is_left_child:
        tree[value] = [parent, vr]
        tree[parent] = [vl, pr]
    else:
        tree[value] = [vl, parent]
        tree[parent] = [pl, vr]
    
    if grandparent != 0:
        if is_parent_left_child:
            tree[grandparent][0] = value
        else:
            tree[grandparent][1] = value

def find_root(tree: dict):
    children = set()
    for node in tree:
        left, right = tree[node]
        if left != 0:
            children.add(left)
        if right != 0:
            children.add(right)
    for node in tree:
        if node not in children:
            return node
    return 0  # если дерево пустое

def print_inorder(tree: dict, node: int):
    if node == 0:
        return
    left, right = tree.get(node, [0, 0])
    print_inorder(tree, left)
    print(node, end=' ')
    print_inorder(tree, right)

for i in range(1, N - 2):
    tree[i] = [0, 0]

    if 2 * i <= N:
        tree[i][0] = 2 * i
    
    if 2 * i + 1 <= N:
        tree[i][1] = 2 * i + 1

for comm in commands:
    switch(comm, tree)

print_inorder(tree, find_root(tree))