from tkinter import Tk
root = Tk()
root.withdraw()
import os
from tkinter.filedialog import askdirectory
import cv2 
import numpy as np 

path = askdirectory(title='Select Brawlhalla Folder')
path = os.path.join(path, "mapArt/Backgrounds/")

for filename in os.listdir(path):
    if filename.endswith(".png") or filename.endswith(".jpg"): 
        print("Blurring: "+os.path.join(path, filename))
        image = cv2.imread(os.path.join(path, filename))
        image = cv2.GaussianBlur(image, (115, 115), 18)
        image = np.uint8(np.double(image) - 10)
        if cv2.imwrite(os.path.join(path, filename), image):
            continue
        else:
            print("Failed to save. Check permissions!")
        continue
    else:
        continue

print("Backgrounds blurred!")