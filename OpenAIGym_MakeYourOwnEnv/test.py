import gymexamples
import gym

env = gym.make('gymexamples/GridWorld-v0')
observation=env.reset(seed=None,options=None)
print(observation)