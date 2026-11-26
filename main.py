#!/usr/bin/env python3
"""Print the robot vacuum's one-line excuse for missing a spot."""

# The vacuum's lidar is very confident about load-bearing crumbs.
def get_line():
    return "My lidar flagged that crumb as a load-bearing wall, so I cleaned around it out of respect for the architecture."


print(get_line())
