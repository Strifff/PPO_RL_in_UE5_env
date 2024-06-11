#!/bin/bash

# Source the Conda script to ensure `conda` command is available
source /Users/axelsolhall/miniconda3/etc/profile.d/conda.sh

# Activate the Conda environment
conda activate PPOUE

# Set the PYTHONHOME and PYTHONPATH to the Conda environment
export PYTHONHOME=/Users/axelsolhall/miniconda3/envs/PPOUE
export PYTHONPATH=/Users/axelsolhall/miniconda3/envs/PPOUE/lib/python3.11/site-packages  # Adjust python version if needed

# Ensure the correct Python executable is used
export PATH=/Users/axelsolhall/miniconda3/envs/PPOUE/bin:$PATH

# Launch Unreal Engine
/Users/axelsolhall/EpicGames/UE_5.4/Engine/Binaries/Mac/UnrealEditor.app/Contents/MacOS/UnrealEditor
