import cv2
import pytesseract # i want to build my own network
import numpy as np

class ImageReader():

    def __init__(self, input):
        self.inputImg = cv2.imread('image.jpg')
