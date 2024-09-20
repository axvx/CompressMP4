# Video Compression Script

This Python script compresses `.mp4` video files to a target file size using FFmpeg. The user can select from available `.mp4` files in the current directory and specify the desired target size (in MB) for the compressed output.

## Features

- **Automatic file listing:** Displays all `.mp4` files in the current directory for easy selection.
- **Custom output file name:** Allows the user to specify the name of the output file.
- **Target file size:** Compresses the video to a specified file size in MB.
- **Video scaling:** Scales down videos with a maximum height of 720 pixels to preserve quality.

## Prerequisites

Before running this script, ensure the following are installed:

1. **Python 3.x**
2. **FFmpeg**: The script relies on FFmpeg to compress the video files. You can install it using:
   - On macOS: `brew install ffmpeg`
   - On Linux (Ubuntu): `sudo apt install ffmpeg`
   - On Windows: [Download from FFmpeg website](https://ffmpeg.org/download.html)
  
     NOTE: Try to add ffmpeg and ffprobe to the PATH or pass directly the path of the binary like this:
     ```
       cmd = [
        '/opt/homebrew/Cellar/ffmpeg/7.0.2_1/bin/1ffmpeg', '-i', input_file_path,
        '-b:v', str(int(target_bitrate_kbps)) + 'k',
        '-bufsize', str(int(target_bitrate_kbps)) + 'k',
        '-maxrate', str(int(target_bitrate_kbps)) + 'k',
        '-vf', "scale=-2:'min(720,ih)'",
        '-threads', '0',
        '-y', output_file_path
    ]
     ```
     

3. **tqdm**: For displaying progress bars.
   - You can install it using `pip`:
     ```bash
     pip install tqdm
     ```

## How to Use

1. **Clone or download the script:**
   ```bash
   git clone https://github.com/your-repo/video-compression-script.git
   cd video-compression-script

2. **Run the script:**
  ```bash
python compress_video.py
 ```

3. **Follow the prompts:**

-The script will display all .mp4 files in the current directory.
-Enter the number corresponding to the video file you want to compress.
-Provide a name for the output file.
-Specify the target file size in MB.

**Example interaction**

Available MP4 files in current directory:
1. example_video.mp4
Enter the number of the file you want to compress or type 'exit' to quit:
1
Enter the name for the output file (e.g., output.mp4):
compressed_example.mp4
Enter the target size in MB (e.g., 50):
50
Starting compression...

**Results**

- **Original video size: 415.7 MB
- **Compressed File: 7.1 MB

<img width="767" alt="image" src="https://github.com/user-attachments/assets/12e33398-5910-4847-a3b2-a62706cb58ef">

**Aspect of the original video:**

<img width="684" alt="image" src="https://github.com/user-attachments/assets/1546e195-3cbe-420f-b508-3a378c238568">

**Compressed video:**

<img width="595" alt="image" src="https://github.com/user-attachments/assets/2d2d4d10-bb03-462e-b0de-cb99ba9d29b3">




