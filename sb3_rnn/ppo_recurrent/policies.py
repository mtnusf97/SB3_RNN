from sb3_rnn.common.recurrent.policies import (
    RecurrentActorCriticCnnPolicy,
    RecurrentActorCriticPolicy,
    RecurrentMultiInputActorCriticPolicy,
)

MlpRnnPolicy = RecurrentActorCriticPolicy
CnnRnnPolicy = RecurrentActorCriticCnnPolicy
MultiInputRnnPolicy = RecurrentMultiInputActorCriticPolicy
