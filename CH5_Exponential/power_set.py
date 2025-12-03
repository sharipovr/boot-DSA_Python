def power_set(input):
    if len(input) == 0:
        return [input]
    
    all_subsets = [[]]
    for i in input:
        new_subsets = []
        for s in all_subsets:
            new_subset = s + [i] 
            new_subsets.append(new_subset)
        all_subsets.extend(new_subsets)

    return all_subsets