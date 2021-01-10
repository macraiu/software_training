import gym
from typing import TypeVar
import random

Action = TypeVar('Action')

class RandomActionWrapper(gym.ActionWrapper):
    def __init__(self, env, epsilon = 0.1):
        super(RandomActionWrapper, self).__init__(env) 
        self.epsilon = epsilon

    def action(self, action: Action) -> Action:
        if random.random() < self.epsilon:
            print('Random!')
            return self.env.action_space.sample()
        return action

def print_env_info(env):
    print(obs)
    print(env.action_space)
    print(env.observation_space)
    print(env.action_space.sample())
    print(env.observation_space.sample())



if __name__ == '__main__':
    env = RandomActionWrapper(gym.make('CartPole-v0'))
    env = gym.wrappers.Monitor(env, 'recording', force=True)
    for i_episode in range(30):
        obs = env.reset()
        total_reward, total_steps = 0.0, 0
        while True:
            env.render()
            action = env.action_space.sample()
            obs, reward, done, _ = env.step(action)
            total_reward += reward
            total_steps += 1
            #if done:
            #    break
    
        print('episode steps: %d    total reward: %.2f' % (total_steps, total_reward))