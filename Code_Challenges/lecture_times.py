# You are given an array of tuples (start, end) representing time intervals for 
# lectures. The intervals may be overlapping. Return the number of rooms that are required.

# For example. [(30, 75), (0, 50), (60, 150)] should return 2.


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


def num_rooms(times):
    # for every item loop through the rest
    # and look for collisions.
    # return max collisions
    max_collisions = 1
    times = sorted(times)
    for index,i in enumerate(times):
        counter = 0
        for j in times[index:]:
            if collision(i,j):
                counter += 1
        if counter > max_collisions:
            max_collisions = counter
    return max_collisions


def collision(time1,time2):
    # returns a boolean 
    # true = the two times collide
    # false = two times do not collide
    if time2[0]<time1[1]:
        return True
    return False

times = [(30, 75), (0, 50), (60, 150)]
print(num_rooms(times))
