# Whisper HPC Automation
Script for running insanely-fast-whisper (https://github.com/Vaibhavs10/insanely-fast-whisper) on HPC systems, specifically on ZIH AlphaCentauri.

## Usage
- batch.sh will launch as many jobs as defined in #SBATCH --array=STARTID-STOPID
- each job will transcribe the n-th file from the given input folder, starting with 0
- eg. `#SBATCH --array=10-14` will transcribe five files numbered 10,11,12,13,14