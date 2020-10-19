import os, glob
from pydub import AudioSegment as am
dir_ = "C:/Users/Lyudmila/Desktop/emotion/test/sad/"
os.chdir(dir_)
count = 0
for file_ in glob.glob("*.wav"):
    file_tmp = am.from_file(file_, format='wav', frame_rate=48000)
#sound = am.from_file("D:/tmp/digits_rus/ноль/010 ноль.wav", format='wav', frame_rate=8000)
#sound = sound.set_frame_rate(16000)
    file_tmp = file_tmp.set_frame_rate(16000)
    file_tmp.export('C:/Users/Lyudmila/Desktop/emotion/test_16000/sad/' + "m_" + file_, format='wav')
    count += 1
print(count)
