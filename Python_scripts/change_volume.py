"""
これから外部モジュールとして使えるようにします！ひとまずできたってことで置いとく
"""
import subprocess
import re
def adjuster(path):
    script = "ffmpeg -i "+path+" -filter:a volumedetect -f null /dev/null"
    #script = "ls"
    #script = ["ffmpeg" , "-i" , "/Users/sotarofurukawa/procon/Python_scripts/audio/Conposition_Audio/out.wav" , "-filter:a" , "volumedetect" , "-f" , "null" , "/dev/null"]
    ret = subprocess.run(script , text=True , shell=True , stdout=subprocess.PIPE , stderr=subprocess.STDOUT).stdout
    result = re.findall('mean_volume: (.*)dB' , ret)
    f_result = float(result[0])
    gap = float((-19.2) - f_result)
    gap = '{:.1f}'.format(gap)
    print(gap)
    second_script = "ffmpeg -i "+path+" -filter:a "+'"volume='+str(gap)+'dB"'+" -y ~/procon/Python_scripts/audio/test.wav"
    subprocess.run(second_script , shell=True)
    #江戸時代

if __name__ == '__main__':
    adjuster()