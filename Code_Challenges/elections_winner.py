def electionsWinners(votes, k):
    
    # loop through the items in votes
    # and see if by adding every single 
    # one of the uncounted votes 
    # that number can exceed the max in the 
    # list
    # if it can that candidate is still in the running
    # else they can't
    
    num_candidates = len(votes)
    current_max = max(votes)
    in_the_running = 0
    num_maxes = 0
    for i in votes:
        if (i + k) > current_max:
            in_the_running += 1
        if i == current_max:
            num_maxes += 1
    if in_the_running == 0 and num_maxes == 1:
        # now check if there are two maxes
        return 1
        
    return in_the_running
    