import os
import sys
from PIL import Image, ImageTk

@staticmethod
def imgSrc(img, raid: str = "") -> str:
    if getattr(sys, 'frozen', False):
        filepath = os.path.dirname(sys.executable)
    elif __file__:
        filepath, filename = os.path.split(os.path.realpath(__file__))

    return os.path.join(filepath, "img", img) if raid == "" else os.path.join(filepath, "img", raid, img)

@staticmethod
def fileSrc(file):
    if getattr(sys, 'frozen', False):
        filepath = os.path.dirname(sys.executable)
    elif __file__:
        filepath, filename = os.path.split(os.path.realpath(__file__))
    return os.path.join(filepath,file)

@staticmethod
def resizeImage(img, newWidth, newHeight):
    pilImage = ImageTk.getimage(img).convert("RGBA")
    oldWidth, oldHeight = pilImage.size
    newImg = pilImage.resize((newWidth, newHeight), Image.LANCZOS)
    newPhotoImage = ImageTk.PhotoImage(newImg)
    return newPhotoImage

@staticmethod
def calculateDropPercentage(raidTotal, dropTotal):
    return round(raidTotal / dropTotal * 100, 2)