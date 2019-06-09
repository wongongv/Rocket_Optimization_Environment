from gym.envs.registration import register

register(
    id='rocket-v0',
    entry_point='rocket_opt.envs:RocketOpt',
)