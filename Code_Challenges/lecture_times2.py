#Too complicated, and unnecessary.
def num_rooms2(times):
    # if there is an overlap as you are going through
    # increase number of rooms needed
    # start checking against new room

    # for example.
    # something that collides with the first room 
    # doesn't particularly collide with the second
    # you have to start checking for collisions in a new place.
    #

    # sort by start time first
    # times = sorted(times)
    # room_dict = {}
    # room_dict[1] = [times[0]]
    # num_rooms = 1
    # flag = True
    # for index,i in enumerate(times):
    #     for j in room_dict:
    #         if collision(i,j):
    #         else:
    #             room_dict[j].append(i)
    #             flag = False
    #             break
    #     if flag:
    #         # there were collisions on everything
    #         num_rooms += 1
    #         room_dict[num_rooms] = [i]
    #     flag = True
    pass