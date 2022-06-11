cons_x, cons_y, noise_range = map(int, input().split())

tree_count = int(input())
for i in range(tree_count):
    tree_x, tree_y = map(int, input().split())
    dist_x = cons_x - tree_x
    dist_y = cons_y - tree_y
    if dist_x**2 + dist_y**2 >= noise_range**2:
        print('silent')
    else:
        print('noisy')

