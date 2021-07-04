import gym
# from gym import error, spaces, utils
# from gym.utils import seeding
import numpy as np


class SleepEnvironment(gym.Env):
    # metadata = {'render.modes': ['human']}
    message = "I am Sleep environmennt but only importing gym lol"

    def __init__(self):
        pass

    def step(self, action):
        a = np.random.rand(2)
        return a

    def reset(self):
        pass

    def render(self, mode='human'):
        pass

    def close(self):
        pass
