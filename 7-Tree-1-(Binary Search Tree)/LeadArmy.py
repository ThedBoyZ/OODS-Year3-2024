class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def print_tree(root, level=0):
    if root is not None:
        print_tree(root.right, level + 1)
        print(' ',end="")
        if level > 0:
            print(' ' * level,end="")
        print(' ' * 4 * level + str(root.val))
        print_tree(root.left, level + 1)

def find_paths(root, current_path=None, all_paths=None):
    if current_path is None:
        current_path = []
    if all_paths is None:
        all_paths = []

    if root is None:
        return []

    current_path.append(root.val)

    # If it's a leaf node, append the path
    if root.left is None and root.right is None:
        all_paths.append(list(current_path))
    else:
        # Recursively find paths, prioritizing the left subtree first (to ensure smaller values)
        if root.left:
            find_paths(root.left, current_path, all_paths)
        if root.right:
            find_paths(root.right, current_path, all_paths)

    current_path.pop()
    return all_paths

def path_sum(path):
    return sum(path)

def remove_paths(root, condition, k):
    paths = find_paths(root)
    removed_paths = []

    while True:
        paths_to_remove = []
        for path in paths:
            path_sum_value = path_sum(path)
            if (condition == 'L' and path_sum_value < k) or \
               (condition == 'EQ' and path_sum_value == k) or \
               (condition == 'M' and path_sum_value > k):
                paths_to_remove.append(path)

        if not paths_to_remove:
            break

        # Sort paths first by the length, then by the sum, and then lexicographically
        paths_to_remove.sort(key=lambda x: (len(x), path_sum(x), x))

        for path in paths_to_remove:
            root = delete_path(root, path)
            removed_paths.append(path)

        paths = find_paths(root)

    return root, removed_paths


def delete_path(root, path):
    if root is None:
        return None

    if root.val == path[0]:
        if len(path) == 1:
            return None
        elif path[1] < root.val:
            root.left = delete_path(root.left, path[1:])
        else:
            root.right = delete_path(root.right, path[1:])
    else:
        if path[0] < root.val:
            root.left = delete_path(root.left, path)
        else:
            root.right = delete_path(root.right, path)
    
    return root

# Input handling and data parsing
input_data = input("Enter <Create City A (BST)>/<Create conditions and deploy the army>: ")
city_data, army_conditions = input_data.split('/')
city_list = list(map(int, city_data.split()))
army_list = army_conditions.split(',')

# Create City A (BST)
root = None
for num in city_list:
    root = insert(root, num)

print("(City A) Before the war:")
print_tree(root)

# Apply the army's conditions
for condition in army_list:
    cond, k = condition.split()
    k = int(k)
    root, removed = remove_paths(root, cond, k)
    if cond == 'L':
        count = 1
        if removed:
            print("--------------------------------------------------")
            print(f"Removing paths where the sum is less than {k}:")
            for path in removed:
                print(f"{count}) {'->'.join(map(str, path))} = {path_sum(path)}")
                count+=1
        else:
            print("--------------------------------------------------")
            print(f"No paths were removed where the sum is less than {k}")
        
    if cond == 'M':
        count = 1
        if removed:
            print("--------------------------------------------------")
            print(f"Removing paths where the sum is greater than {k}:")
            for path in removed:
                print(f"{count}) {'->'.join(map(str, path))} = {path_sum(path)}")
                count+=1
        else:
            print("--------------------------------------------------")
            print(f"No paths were removed where the sum is greater than {k}")

    if cond == 'EQ':
        count = 1
        if removed:
            print("--------------------------------------------------")
            print(f"Removing paths where the sum is equal to {k}:")
            for path in removed:
                print(f"{count}) {'->'.join(map(str, path))} = {path_sum(path)}")
                count+=1
        else:
            print("--------------------------------------------------")
            print(f"No paths were removed where the sum is equal to {k}")
            
    print("--------------------------------------------------")
    print("(City A) After the war:")
    print_tree(root)

if root is None:
    print("City A has fallen!")
