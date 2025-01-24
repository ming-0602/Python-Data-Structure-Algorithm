def pageCount(n, p):
    # Write your code here

    frontpage = p // 2
    backpage = (n // 2) - (p // 2)

    return min(frontpage, backpage)