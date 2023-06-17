from typing import NamedTuple, Tuple

import torch as th
from stable_baselines3.common.type_aliases import TensorDict


class RNNStates(NamedTuple):
    pi: th.Tensor
    vf: th.Tensor


class RecurrentRolloutBufferSamples(NamedTuple):
    observations: th.Tensor
    actions: th.Tensor
    old_values: th.Tensor
    old_log_prob: th.Tensor
    advantages: th.Tensor
    returns: th.Tensor
    rnn_states: RNNStates
    episode_starts: th.Tensor
    mask: th.Tensor


class RecurrentDictRolloutBufferSamples(NamedTuple):
    observations: TensorDict
    actions: th.Tensor
    old_values: th.Tensor
    old_log_prob: th.Tensor
    advantages: th.Tensor
    returns: th.Tensor
    rnn_states: RNNStates
    episode_starts: th.Tensor
    mask: th.Tensor
