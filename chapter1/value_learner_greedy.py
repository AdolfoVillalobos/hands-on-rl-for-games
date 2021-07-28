import random

reward = [1.0, 0.5, 0.2, 0.5, 0.6]
arms = len(reward)
episodes = 100
learning_rate = .1
Value = [0.0] * arms
print(Value)


def greedy(values):
    return values.index(max(values))


# Learning
for i in range(episodes):
    action = greedy(Value)
    Value[action] = Value[action]+learning_rate*(reward[action]-Value[action])

print(Value)
