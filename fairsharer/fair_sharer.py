def fair_sharer(values, num_iterations, share=0.1):
    """
    Runs num_iterations.
    In each iteration the highest value in values gives a fraction (share)
    to both the left and right neighbor. The leftmost field is considered
    the neighbor of the rightmost field.
    
    Args:
        values: 1D array of values (list or numpy array)
        num_iterations: Integer to set the number of iterations
        share: Fraction to distribute to neighbors
    """
    values_new = values[:]
    n = len(values_new)

    for _ in range(num_iterations):
        # Find the highest value
        max_index = values_new.index(max(values_new))
        max_value = values_new[max_index]
        
        # Calculate the distributed value
        distributed_value = int(max_value * share)
        
        # Distribute the value to the neighbors
        left_neighbor = (max_index - 1) % n
        right_neighbor = (max_index + 1) % n
        values_new[left_neighbor] += distributed_value
        values_new[right_neighbor] += distributed_value

        # Reduce the value of the highest value
        values_new[max_index] -= 2 * distributed_value

    return values_new