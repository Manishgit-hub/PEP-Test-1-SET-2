def countDuplicates(name, price, weight):
    seen = set()
    duplicate_count = 0
    for i in range(len(name)):
        product = (name[i], price[i], weight[i])
        if product in seen:
            duplicate_count += 1
        else:
            seen.add(product)
    return duplicate_count