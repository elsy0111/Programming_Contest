from doctest import OutputChecker
import subprocess

# script = "ffmpeg -y -i audio/debug.mp3 -af atrim=start_sample=44200:end_sample=120000 audio/output.mp3"
start_sample = 1
end_sample = 96000
out = 'audio/Conposition_Audio/split/out.wav'
script = "ffmpeg -y -i audio/Conposition_Audio/out.wav -af atrim=start_sample=\
" + str(start_sample) + ":end_sample=" + str(end_sample) + " " +  out

subprocess.run(script,shell = True)
print(script)
