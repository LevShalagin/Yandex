recipes = {
    1: '1',
    2: '2',
}

def has_cycles(graph):
    """Проверяет, есть ли циклы в графе (через DFS с пометками)"""
    visited = set()
    recursion_stack = set()

    def dfs(node):
        if node in recursion_stack:
            return True  # найден цикл!
        if node in visited:
            return False

        visited.add(node)
        recursion_stack.add(node)

        for neighbor in graph.get(node, set()):
            if dfs(neighbor):
                return True

        recursion_stack.remove(node)
        return False

    for node in graph:
        if dfs(node):
            return True
    return False


def get_full_recipe(recipe: str):
    res = recipe[:]

    if set(list(res)) in (set(['1', '2']), set(['2', '1'])):
        return res

    for ch in res:
        if ch in recipes[int(ch)]:
            return None
        if ch not in ('1', '2'):
            res = res.replace(ch, recipes[int(ch)])

    return get_full_recipe(res)


def solution(A: int, B: int, S: str) -> int:
    recipe = get_full_recipe(S)
    if recipe is None:
        return 0
    if recipe.count('1') <= A and recipe.count('2') <= B:
        return 1
    return 0


for ind in range(3, int(input()) + 1):
    recipes[ind] = ''.join(input().split())[1::]

for _ in range(int(input())):
    A, B, S = list(map(int, input().split()))
    print(solution(A, B, str(S)), end='')

'''
7
3 1 1 2
2 1 3
3 4 3 4
1 7
1 6
3
8 4 5
9 2 5
10 10 6
'''