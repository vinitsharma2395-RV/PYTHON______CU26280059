import ast


nested_list = ast.literal_eval(input("Enter a nested list (example: [[1, 2], [3, [4]]]): "))
flattened_list = []


def flatten(items):
    for item in items:
        if isinstance(item, list):
            flatten(item)
        else:
            flattened_list.append(item)


flatten(nested_list)
print("Flattened list:", flattened_list)
