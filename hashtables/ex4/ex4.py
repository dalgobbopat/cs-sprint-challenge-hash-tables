def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    # Create a hashtable to store the numbers 
    hashtable = {}
    # Put the results in an array to to be able to see which are positive and negative
    result = []
    # If number has a negative in hashtable print results 
    for i in a:
        if i is -i in hashtable:
            print(i)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
