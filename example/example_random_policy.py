import gym
import numpy as np
import time

itr = 10
steps = 1000
env = gym.make('rocket_opt:rocket-v0')
for _ in range(itr):
	env.reset()	
	for i in range(steps):
		action = np.random.randint(4)
		_,re,done,_ = env.step(action)
		env.render()
		print(re)
		if done:
			break
	x = input("type in y if you want to quit:")
	if x == 'y':
		break
