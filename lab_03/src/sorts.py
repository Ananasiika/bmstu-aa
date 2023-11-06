def comb_sort(arr):
    gap = len(arr)
    shrink_factor = 1.3

    while gap >= 1:
        gap = int(gap / shrink_factor)

        i = 0
        while i + gap < len(arr):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
            i += 1

    return arr



class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert_node(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert_node(root.left, value)
    else:
        root.right = insert_node(root.right, value)
    return root

def centered_traversal(root, sorted_list):
    if root:
        centered_traversal(root.left, sorted_list)
        sorted_list.append(root.value)
        centered_traversal(root.right, sorted_list)

def binary_tree_sort(arr):
    root = None
    for element in arr:
        root = insert_node(root, element)

    sorted_list = []
    centered_traversal(root, sorted_list)
    return sorted_list



def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged