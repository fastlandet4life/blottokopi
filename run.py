

def improved_computer_strategy(n_battalions, n_fields):
    battalions = np.zeros(n_fields, dtype=int)
    base_allocation = n_battalions // n_fields
    random_weight = np.random.normal(1.0, 0.3, size=n_fields)
    random_weight = np.maximum(random_weight, 0)  
    
    weighted_allocation = np.floor(base_allocation * random_weight).astype(int)
    allocated = weighted_allocation.sum()
    remaining = n_battalions - allocated
    
    while remaining > 0:
        index = np.random.randint(n_fields)
        battalions[index] += 1
        remaining -= 1
    
    battalions += weighted_allocation
    return battalions



def improved_player_strategy(n_battalions, n_fields):
    battalions = np.zeros(n_fields, dtype=int)
    
    strong_fields = np.random.randint(1, n_fields//2)  # Tilfeldig antall sterke felt
    bluff_fields = np.random.randint(1, n_fields//2)  # Tilfeldig antall bløff felt
    remaining_fields = n_fields - strong_fields - bluff_fields

    # Tilfeldig fordeler sterke og bløffe felt
    strong_allocation = (n_battalions * 0.5) // strong_fields
    bluff_allocation = (n_battalions * 0.1) // bluff_fields
    remaining_allocation = (n_battalions - strong_allocation * strong_fields - bluff_allocation * bluff_fields) // remaining_fields

    # Tildel bataljoner til de utvalgte feltene
    battalions[:strong_fields] = strong_allocation
    battalions[strong_fields:strong_fields + bluff_fields] = bluff_allocation
    battalions[strong_fields + bluff_fields:] = remaining_allocation

    # Fordel gjenværende bataljoner tilfeldig
    remaining_battalions = n_battalions - battalions.sum()
    while remaining_battalions > 0:
        index = np.random.randint(n_fields)
        battalions[index] += 1
        remaining_battalions -= 1
    
    return battalions


import blotto
blotto.Run(6,100)
