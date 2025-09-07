from tkinter.filedialog import askopenfilename
from moviepy import VideoFileClip

vid = askopenfilename()
video = VideoFileClip(vid)

aud = video.audio
aud.write_audiofile("audio.mp3")

print("---END---")
