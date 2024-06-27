import argparse
import json
import subprocess
import uuid
import os


def read_config(config_file):
    with open(config_file, "r") as f:
        config = json.load(f)

    return config


def excecute_whisper(
    file_path,
    output_path,
    language,
    flash,
    diarization_model,
    hf_token,
    min_speakers,
    max_speakers,
):
    print(f"Transcribing {file_path}")
    command = f'insanely-fast-whisper --file-name="{file_path}" --language="{language}" --transcript-path="{output_path}" --diarization_model="{diarization_model}" --hf-token="{hf_token}" --timestamp="word" --min-speakers="{min_speakers}" --max-speakers="{max_speakers}" --batch-size="8"'
    if flash:
        command += '--flash="True"'
    subprocess.run(command, shell=True)
    print(command)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Manage Diarization")
    parser.add_argument("config_file", type=str, help="Path to the JSON file")
    parser.add_argument("data_folder", type=str, help="Path to audio folder")
    parser.add_argument("output_folder", type=str, help="Path to output folder")
    parser.add_argument("file_num", type=int, help="File number")
    parser.add_argument("hf_token", type=str, help="Hugging Face Token")

    args = parser.parse_args()

    config = read_config(args.config_file)

    files = os.listdir(args.data_folder)
    files.sort()

    orig_name = files[args.file_num]
    input_file = os.path.join(args.data_folder, orig_name)
    temp_file = f"{uuid.uuid4().hex}.mp3"

    temp_file = input_file

    output_path = os.path.join(args.output_folder, f"{orig_name[:-4]}_output.json")

    excecute_whisper(
        temp_file,
        output_path,
        config["language"],
        config["flash"],
        config["diarization_model"],
        args.hf_token,
        config["min_speakers"],
        config["max_speakers"],
    )

    os.remove(temp_file)
