from gymexamples.envs.grid_world import GridWorldEnv
from gym.envs.registration import register

register(
    id='gymexamples/GridWorld-v0',
    entry_point='gymexamples.envs:GridWorldEnv',
    max_episode_steps=300,
)

