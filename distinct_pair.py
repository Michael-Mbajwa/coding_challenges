def distinct_pair(s):
    """A short Python function that takes a sequence of integer values and
    determines if there is a distinct pair of numbers in the sequence whose product is odd."""
    pairs_with_odd_products = []
    len_pairs = len(pairs_with_odd_products)
    n = len(s)
    for a in range(n):
        initial_value = s[a]
        for b in range(n):
            if a != b:
                next_value = s[b]
                product = initial_value * next_value
                if product % 2 != 0:
                    tuple_product_pairs = tuple([initial_value, next_value])
                    x, y = tuple_product_pairs
                    if (x, y) not in pairs_with_odd_products and (y, x) not in pairs_with_odd_products:
                        pairs_with_odd_products.append(tuple_product_pairs)

    return pairs_with_odd_products


print(distinct_pair([2, 3, 4, 5, 7, 9, 3, 2]))