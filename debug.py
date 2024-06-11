import sys

import unreal

unreal.log("Python executable: " + sys.executable)

import torch

# tensor test
a = torch.tensor([1, 2, 3])
print(a)
b = torch.tensor([4, 5, 6])
c = a + b
print(c)

# export PYTHONPATH=/opt/homebrew/Caskroom/miniforge/base/envs/PPOUE/lib/python3.11/site-packages
# cd /Users/your_username/EpicGames/UE_5.4/ && ./UE4Editor
# ./EpicGames/UE_5.4/Engine/Binaries/Mac/UnrealEditor.app/Contents/MacOS/UnrealEditor

#
# export PYTHONHOME=/Users/axelsolhall/miniconda3/envs/PPOUE
# export PYTHONPATH=/Users/axelsolhall/miniconda3/envs/PPOUE
