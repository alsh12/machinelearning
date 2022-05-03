import gym
import numpy as np

import gym_bandits
from .bandit import BanditTwoArmedHighLowFixed

from matplotlib import pyplot as plot

# Invoke an environment in which one of the bandits has a higher rewards and the other has a lesser reward

env = gym.make("BanditTwoArmedHighLowFixed-v0")

# Repeat the process given below and see which Agent has a bigger reward

env.reset()
observation, reward, done, info = env.step(1)
print(observation,reward)

observation, reward, done, info = env.step(0)

print(observation,reward)

