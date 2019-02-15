# About

Adapt [this repo](https://github.com/floodsung/DDPG) for this [Wechat Jump game](https://github.com/gooooloo/gym-android-wechat-jump).

# DDPG

Reimplementing DDPG from Continuous Control with Deep Reinforcement Learning based on OpenAI Gym and Tensorflow

[http://arxiv.org/abs/1509.02971](http://arxiv.org/abs/1509.02971)

It is still a problem to implement Batch Normalization on the critic network. However the actor network works well with Batch Normalization.

Some Mujoco environments are still unsolved on OpenAI Gym.


## How to use

```
git clone https://github.com/songrotek/DDPG.git
cd DDPG
python gym_ddpg.py

```
If you want to change the Network type, change import in ddpg.py such as 

```
from actor_network_bn import ActorNetwork
to
from actor_network import ActorNetwork
```

## Reference
1 [https://github.com/rllab/rllab](https://github.com/rllab/rllab)

2 [https://github.com/MOCR/DDPG](https://github.com/MOCR/DDPG)

3 [https://github.com/SimonRamstedt/ddpg](https://github.com/SimonRamstedt/ddpg)




