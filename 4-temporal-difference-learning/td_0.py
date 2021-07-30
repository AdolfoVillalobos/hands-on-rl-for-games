import numpy as np
from tqdm import tqdm
import random

gamma = .5
reward_size = -1
grid_size = 4
alpha = .5
terminations = [[0, 0], [grid_size-1, grid_size-1]]
actions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
episodes = 10000

V = np.zeros((grid_size, grid_size))
returns = {(i, j): list() for i in range(grid_size) for j in range(grid_size)}
deltas = {(i, j): list() for i in range(grid_size) for j in range(grid_size)}
states = [[i, j] for i in range(grid_size) for j in range(grid_size)]


def generate_initial_state():
    init_state = random.choice(states[1:-1])
    return init_state


def generate_next_action():
    return random.choice(actions)


def take_action(state, action):
    if list(state) in terminations:
        return 0, None
    final_state = np.array(state)+np.array(action)
    if -1 in list(final_state) or grid_size in list(final_state):
        final_state = state
    return reward_size, list(final_state)


for it in tqdm(range(episodes)):
    state = generate_initial_state()
    while True:
        action = generate_next_action()
        reward, final_state = take_action(state, action)
        if final_state is None:
            break
        before = V[state[0], state[1]]
        V[state[0], state[1]] += alpha * \
            (reward+gamma*V[final_state[0],
             final_state[1]]-V[state[0], state[1]])
        deltas[state[0], state[1]].append(
            float(np.abs(before-V[state[0], state[1]])))
        state = final_state

print(V)
