import gym

from agents.noisy_dqn import NoisyDQNAgent
from common.wrappers import make_atari, wrap_deepmind, wrap_pytorch
from common.utils import mini_batch_train_frames

env_id = "PongNoFrameskip-v4"
env    = make_atari(env_id)
env    = wrap_deepmind(env)
env    = wrap_pytorch(env)

MAX_EPISODES = 1000
MAX_STEPS = 500
BATCH_SIZE = 32

agent = NoisyDQNAgent(env, use_conv=True)
episode_rewards = mini_batch_train_frames(env, agent, MAX_EPISODES, MAX_STEPS, BATCH_SIZE)
