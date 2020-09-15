def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # ========= create dictionary =========
    weight_dict = dict()

    # ========= add weight to the dict =========
    for item in range(len(weights)):
        weight_dict[weights[item]] = item

    for item in range(len(weights)):
        #  ========= subtract each item weight from the limit weight =========
        remainder = limit - weights[item]
        #  ========= if the remainder is a weight in the list, return both of it with remainder =========
        if remainder in weight_dict:
            return max(item, weight_dict[remainder]), min(item, weight_dict[remainder])
    return None
