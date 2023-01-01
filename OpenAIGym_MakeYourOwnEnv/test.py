import gymexamples
import gymnasium

env = gymnasium.make('gymexamples/GridWorld-v0')
print(env.metadata)