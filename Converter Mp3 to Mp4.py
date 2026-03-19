import os
import subprocess

# Root folder (where the script is located)
root_folder = os.path.dirname(os.path.abspath(__file__))

print("Scanning for audio files...")

for foldername, subfolders, filenames in os.walk(root_folder):
    for filename in filenames:
        if filename.lower().endswith((".m4a", ".mp3")):

            input_path = os.path.join(foldername, filename)
            output_path = os.path.join(foldername, os.path.splitext(filename)[0] + ".mp4")

            if os.path.exists(output_path):
                print(f"Skipping (exists): {output_path}")
                continue

            print(f"Converting: {input_path}")

            command = [
                "ffmpeg",
                "-y",
                "-f", "lavfi",
                "-i", "color=c=black:s=1280x720:r=30",
                "-i", input_path,
                "-shortest",
                "-c:v", "libx264",
                "-c:a", "aac",
                "-b:a", "192k",
                "-pix_fmt", "yuv420p",
                output_path
            ]

            subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

print("Done.")