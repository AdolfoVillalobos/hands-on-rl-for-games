import gym

env = gym.make('CartPole-v0')
env.reset()

for i in range(20):
    observation = env.reset()
    for t in range(100):
        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print(f"Episode finished after {t+1} timesteps")
            break
env.close()


# Action space
print(env.action_space)

# Observation space
print(env.observation_space)
