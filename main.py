
import time
import os
os.add_dll_directory(r'C:\Program Files\VideoLAN')
import vlc
import numpy as np
# import cv2
# import matplotlib.pyplot as plt


# test_image = cv2.imread("C:\\Users\\joesi\\Documents\\BlogStuff_Cdrive\\ImageSonification\\hubble_freggs.jpeg")
#
# ##Show the image
# plt.imshow(test_image)
# plt.axis("off")     ## This removes the axis so it just shows the image
# plt.show()
#
framerate = 44100
t = np.linspace(0,5, framerate*5)
tone = np.sin(2*np.pi*440*t)

soundfile = vlc.MediaPlayer(tone)


time.sleep(5)

