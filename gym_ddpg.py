import filter_env
from ddpg import *
import gc
gc.enable()

import gym_android_wechat_jump
ENV_NAME = 'android-wechat-jump-v0'
EPISODES = 100000
TEST = 5

def main():
    env = filter_env.makeFilteredEnv(gym.make(ENV_NAME))
    agent = DDPG(env)
    # env.monitor.start('experiments/' + ENV_NAME,force=True)

    for episode in range(EPISODES):
        state = env.reset()
        state = np.ravel(state)
        print("episode:",episode)
        # Train
        for step in range(99999):
            action = agent.noise_action(state)
            next_state,reward,done,_ = env.step(action)
            next_state = np.ravel(next_state)
            agent.perceive(state,action,reward,next_state,done)
            state = next_state
            if done:
                break
        # Testing:
        if episode % 100 == 0 and episode >= 100:
            total_reward = 0
            for i in range(TEST):
                state = env.reset()
                state = np.ravel(state)
                for j in range(99999):
                    #env.render()
                    action = agent.action(state) # direct action for test
                    state,reward,done,_ = env.step(action)
                    state = np.ravel(state)
                    total_reward += reward
                    if done:
                        break
            ave_reward = total_reward/TEST
            print('episode: ',episode,'Evaluation Average Reward:',ave_reward)
    # env.monitor.close()

if __name__ == '__main__':
    main()
