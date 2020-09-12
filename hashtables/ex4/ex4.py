def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # ========= create dictionary and list =========
    number_dict = dict()
    result = []

    # ========= add each item to dictionary =========
    for num in a:
        number_dict[num] = num

        # ========= if positive num and negative num exist in the dict, add converted absolute value to the array =========
        if num and -num in number_dict:
            result.append(abs(num))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
