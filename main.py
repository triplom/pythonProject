## Exercise A ##
from typing import List

Actions = ["right(+1)"], ["left (-1)"], ["up (-10)"], ["down (+10)"]
list(enumerate(Actions))

from random import random

actions: list[int] = [+1, -1, -10, +10]


def next_state(state: object, action: object) -> object:
    if action == "up" and state > 10:
        return state - 10
    elif action == "down" and state < 91:
        return state + 10
    elif action == "left" and state % 10 != 1:
        return state - 1
    elif action == "right" and state % 10 != 0:
        return state + 1
    else:
        return state


next_state(99, 3)
print(next_state(1, 0))


## Exercise B
def reward(state):
    if state == 100:
        reward = 100
    else:
        reward = 0


## Exercise C
def random_action():
    return random.choice(["up", "down", "left", "right"])


## Exercise D

def run(state):
    total_reward = 0
    while actions < 1000:
        action = random_action()
        new_state: object = next_state(state, action)
        reward = reward(new_state)
        total_reward += reward
        state = new_state
        actions += 1
        if state == 100:
            return total_reward

    return total_reward


# Exercise F
episodes = 30
rewards = []
steps_to_goal = []
runtimes = []


def run_episode():
    pass


for episode in range(episodes):
    run_episode()
    rewards.append(reward)
    steps_to_goal.append(actions)
    runtimes.append(actions)

# Exercise F
avg_reward = sum(rewards) / episodes
avg_steps = sum(steps_to_goal) / episodes
avg_runtime = sum(runtimes) / episodes

print(f"Average Reward per Step: {avg_reward}")
print(f"Average Steps to Reach Goal: {avg_steps}")
print(f"Average Runtime: {avg_runtime} steps")