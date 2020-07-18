# 07162020
# TODO
# need to try for more test cases/ need to write a unit test for this

# You are given an array of tuples (start, end) representing time intervals for 
# lectures. The intervals may be overlapping. Return the number of rooms that are required.

# For example. [(30, 75), (0, 50), (60, 150)] should return 2.

# check lecture_times2 for iplimentation that returns more details.



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
