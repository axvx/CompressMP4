import subprocess
import os
import sys
from tqdm import tqdm


def list_mp4_files(directory):
    return [f for f in os.listdir(directory) if f.endswith('.mp4')]


def compress_video(input_file_path, output_file_path, target_size_MB):
    file_size_MB = os.path.getsize(input_file_path) / (1024 * 1024)
    cmd = ['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1',
           input_file_path]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    duration_seconds = float(result.stdout.decode())

    target_bitrate_kbps = (target_size_MB * 8 * 1024) / duration_seconds
    current_bitrate_kbps = (file_size_MB * 8 * 1024) / duration_seconds

    if file_size_MB > target_size_MB:
        bitrate_ratio = target_size_MB / file_size_MB
        target_bitrate_kbps = current_bitrate_kbps * bitrate_ratio

    cmd = [
        'ffmpeg', '-i', input_file_path,
        '-b:v', str(int(target_bitrate_kbps)) + 'k',
        '-bufsize', str(int(target_bitrate_kbps)) + 'k',
        '-maxrate', str(int(target_bitrate_kbps)) + 'k',
        '-vf', "scale=-2:'min(720,ih)'",
        '-threads', '0',
        '-y', output_file_path
    ]

    print("Starting compression...")
    for _ in tqdm(subprocess.run(cmd, stderr=subprocess.PIPE)):
        pass  # The tqdm iterator is used here for visualization


def main():
    while True:
        print("Available MP4 files in current directory:")
        files = list_mp4_files('.')
        for idx, file in enumerate(files):
            print(f"{idx + 1}. {file}")
        print("Enter the number of the file you want to compress or type 'exit' to quit:")

        choice = input()
        if choice.lower() == 'exit':
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(files):
            input_file_path = files[int(choice) - 1]
            output_file_path = input("Enter the name for the output file (e.g., output.mp4): ")
            target_size_MB = float(input("Enter the target size in MB (e.g., 50): "))
            compress_video(input_file_path, output_file_path, target_size_MB)
        else:
            print("Invalid input, please try again.")


if __name__ == "__main__":
    main()
