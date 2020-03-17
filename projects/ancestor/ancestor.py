def earliest_ancestor(ancestors, starting_node):
    # dictionary of child:[parents]
    forebears = {pair[1]:tuple(i[0] for i in ancestors if i[1] == pair[1]) 
                        for pair in ancestors}
    
    # return -1 if child has no parents
    if starting_node not in forebears.keys():
        return -1
    
    generation = forebears[starting_node]
    # Check each generation of ancestors for parents
    #   until we reach the oldest generation
    while not set(generation).isdisjoint(forebears.keys()):
        older_generation = []
        for member in generation:
            if member in forebears.keys():
                older_generation.extend(forebears[member])
        generation = older_generation
    
    # return ancestor with lowest ID
    return min(generation)
