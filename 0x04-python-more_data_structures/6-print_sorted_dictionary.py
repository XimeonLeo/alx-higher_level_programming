def print_sorted_dictionary(a_dictionary):
    order = list(a_dictionary.keys())
    order.sort()
    for k in order:
        print(f"{k}: {a_dictionary.get(k)}")
