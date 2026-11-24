from math import dist


def gripper_state(thumb, index, closed, close_threshold=0.08, open_threshold=0.14):
    distance = dist(thumb, index)
    return distance < (open_threshold if closed else close_threshold)
