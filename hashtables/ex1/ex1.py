def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    # Seach for two items whose sum weights equals the weight limit 
    # Make a dict of the weights
    weights_dict = {}

    # if the lenght of the weights is less than 1 return None 

    if len(weights) <= 1:
        return None

    for i in range(len(weights)):
        curr = weights[i]
        # find difference between the limit and the current index value
        difference = limit - curr
        print("DIFFERENCE", difference)
        # create a condition checking if the difference is in the weights_dic
        if difference in weights_dict:
            print("RETURNING", (i, weights_dict[difference]))
            return (i, weights_dict[difference])
        else:
            #if not in dict assign the value of the current index to the index loop
            weights_dict[curr] = i
