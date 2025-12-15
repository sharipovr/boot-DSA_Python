def tsp(cities, paths, dist):
    """
    Solves the Traveling Salesman Problem using brute force.
    Checks if there exists a path through all cities with distance less than dist.
    
    Args:
        cities: List of city numbers (starting from 0)
        paths: Distance matrix where paths[i][j] is the distance from city i to city j
        dist: The distance threshold to beat
    
    Returns:
        True if there exists a path with total distance < dist, False otherwise
    """
    # Use the permutations function to get all possible paths through the given cities
    all_paths = permutations(cities)
    
    # Iterate over each possible path (permutation)
    for path in all_paths:
        # Sum the distances between each city in the path using the paths matrix
        total_distance = 0
        
        # Inner loop to sum distances of consecutive city pairs within a single path
        for i in range(len(path) - 1):
            city_from = path[i]
            city_to = path[i + 1]
            total_distance += paths[city_from][city_to]
        
        # If the total distance of the path is less than the given dist, return True
        if total_distance < dist:
            return True
    
    # If no short paths were found, return False
    return False


def verify_tsp(paths, dist, actual_path):
    """
    Verifies if a given path has total distance less than the threshold.
    This runs in polynomial time, demonstrating that TSP is in NP.
    
    Args:
        paths: A matrix where paths[cityA][cityB] holds the distance from cityA to cityB
        dist: The distance threshold we are trying to find a path shorter than
        actual_path: The path we are trying to verify (list of city indices)
    
    Returns:
        True if the path's total distance is less than dist, False otherwise
    """
    # Loop over each city in the actual path
    total_distance = 0
    
    # Sum the distance between each city in the actual path
    for i in range(len(actual_path) - 1):
        city_from = actual_path[i]
        city_to = actual_path[i + 1]
        total_distance += paths[city_from][city_to]
    
    # If the sum is less than dist, return True, otherwise return False
    return total_distance < dist


# don't touch below this line


def permutations(arr):
    res = []
    res = helper(res, arr, len(arr))
    return res


def helper(res, arr, n):
    if n == 1:
        tmp = arr.copy()
        res.append(tmp)
    else:
        for i in range(n):
            res = helper(res, arr, n - 1)
            if n % 2 == 1:
                arr[n - 1], arr[i] = arr[i], arr[n - 1]
            else:
                arr[0], arr[n - 1] = arr[n - 1], arr[0]
    return res
