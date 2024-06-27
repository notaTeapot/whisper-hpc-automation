#!/bin/bash
#SBATCH --array=0-100
#SBATCH --partition=alpha
#SBATCH --nodes=1
#SBATCH --mem=20G
#SBATCH --gres=gpu:1 
#SBATCH --time=02:00:00

PYTHON_ENV="<VENV-FOLDER>/bin/activate"
PYTHON_SCRIPT="./main.py"
CONFIG_FILE="./config.json"
DATA_FOLDER="./data"
OUTPUT_FOLDER="./output"
HF_TOKEN="<YOUR-HF-TOKEN>"

module load release/23.04 GCCcore/11.3.0 GCC/11.3.0 OpenMPI/4.1.4 Python/3.10.4 FFmpeg

source $PYTHON_ENV

echo "$SLURM_ARRAY_TASK_ID Diarizing $SLURM_ARRAY_JOB_ID"

python $PYTHON_SCRIPT $CONFIG_FILE $DATA_FOLDER $OUTPUT_FOLDER $SLURM_ARRAY_TASK_ID $HF_TOKEN
