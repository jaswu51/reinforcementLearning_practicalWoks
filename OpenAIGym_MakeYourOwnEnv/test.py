import gymexamples
import gymnasium

<<<<<<< HEAD
env = gym.make('gymexamples/GridWorld-v0')
observation=env.reset(seed=None,options=None)
print(observation)
=======
env = gymnasium.make('gymexamples/GridWorld-v0')
print(env.metadata)
>>>>>>> parent of 3913841 (push)
