import subprocess

script = "ffmpeg -y -i audio/debug.mp3 -af atrim=start_sample=44200:end_sample=120000 audio/output.mp3"

subprocess.run(script,shell = True)