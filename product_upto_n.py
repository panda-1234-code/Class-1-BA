
def product_upto_n(n):
    product: int = 1
    for i in range(1, n + 1):
        product *= i
    return product
 print(product_upto_n(5))
