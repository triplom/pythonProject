## Exercise A ##
Actions = ["right(1)"], ["left (-1)"], ["up (-10)"], ["down (10)"]
list(enumerate(Actions))

from random import random

actions = [1, -1, -10, 10]


def next_state(state, action):
    next_state1 = state + actions[action]
    if next_state1 < 0 or next_state1 > 100:
        next_state1 = state
    # Action left
    elif state % 10 == 0 and action == 0:
        next_state1 = state
    # Action right
    elif state % 10 == 1 and action == 1:
        next_state1 = state
    # Action up
    elif state <= 10 and action == 2:
        next_state1 = state
    # Action up
    elif state > 10 and action == 3:
        next_state1 = state
    return next_state1


next_state(99, 3)
print(next_state(1, 0))

## Exercise B
def reward (state) :
    if next_state == 100:
        reward = 100
    else:
        reward = 0


## Exercise C

random_action=random.randint(0,3)


## Exercise d

while state < 1000 or state != 100:
    actions = random_action
