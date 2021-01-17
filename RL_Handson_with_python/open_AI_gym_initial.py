# OPENAIR GYM AND UNIVERSE
# DEEPMIND LAB
# RL-GLUE
# PROJECT MALMO
# VIZDOOM

import gym

#env = gym.make('CarRacing-v0')
#env = gym.make('CartPole-v0')
env = gym.make('BipedalWalker-v2')

#from gym import envs
#print(envs.registry.all())

for i_episode in range(30):
    observation = env.reset()
    for t in range(500):
        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("{} timesteps taken for the episode".format(t+1))
            break
