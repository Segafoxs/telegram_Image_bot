import cv2
import numpy as np

def grayPhoto(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(f"downloads\\gray.jpg", gray)

def blurPhoto(img):
    blur = cv2.blur(img, (5, 5))
    cv2.imwrite(f"downloads\\blur.jpg", blur)

def gausPhoto(img):
    gaus = cv2.GaussianBlur(img, (5, 5), 0)
    cv2.imwrite(f"downloads\\gaus.jpg", gaus)

def sharpNessPhoto(img):
    gaussian_photo = cv2.GaussianBlur(img, (5, 5), 0)
    kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    rez_g_photo = cv2.filter2D(gaussian_photo, -1, kernel)
    cv2.imwrite(f"downloads\\sharpNess.jpg", rez_g_photo)