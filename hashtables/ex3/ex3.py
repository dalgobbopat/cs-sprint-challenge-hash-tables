def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    inner_array = []
    input_length = len(arrays)

    for x in arrays:
        for y in x:
            if y not in cache:
                cache[y] = 1
            else:
                cache[y] += 1
            if cache[y] == input_length:
                inner_array.append(y)
    return inner_array


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
