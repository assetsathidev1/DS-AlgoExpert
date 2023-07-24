"""
Array of Products
input: [5, 1, 4, 2]
output: [8, 40, 10, 20]

trick is: find all left products and right products seperatly and then multiply them
"""


# o(n^2) time | o(n) in space
def arrayOfProducts(array):
    out_array = []
    for i in range(len(array)):
        p = 1
        for j in range(len(array)):
            if i == j:
                continue
            p *= array[j]
        out_array.append(p)
    return out_array



# o(n) in time | o(n) in space
def arrayOfProducts(array):
    l_products = [1 for _ in range(len(array))]
    r_products = [1 for _ in range(len(array))]
    out_array = [1 for _ in range(len(array))]

    lp = 1
    for i in range(len(array)):
        l_products[i] = lp
        lp *= array[i]

    rp = 1
    i = len(array)-1
    while i >= 0:
        r_products[i] = rp
        rp *= array[i]
        i -= 1

    for i in range(len(array)):
        out_array[i] = l_products[i] * r_products[i]
    
    return out_array
