import subprocess

# script = "ffmpeg -y -ss 50 -to 60 -i audio/debug.mp3 -c copy audio/output.mp3"
script = "ffmpeg -y -i audio/debug.mp3 -af atrim=start_sample=44200:end_sample=120000 audio/output.mp3"

subprocess.run(script,shell = True)
