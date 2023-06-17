import os
from sb3_rnn.ppo_recurrent.ppo_recurrent import RecurrentPPO

# Read version from file
# version_file = os.path.join(os.path.dirname(__file__), "version.txt")
# with open(version_file) as file_handler:
#     __version__ = file_handler.read().strip()
__version__ = '0.0.1'

__all__ = [
    "RecurrentPPO",
]
