#-*-coding: utf-8-*-
###Resimden Text Cekme###

import numpy as np
import cv2
from PIL import Image
import pytesseract

#ilk olarak pytesseract kütüphanesi kurulmalıdır.	
#sudo pip install pytesseract		
#sudo apt-get install tesseract-ocr

img=cv2.imread('resimler/text.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
thres=cv2.threshold(gray,0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
#gray = cv2.medianBlur(gray, 3)

#lang ile farklı diller için resimden text çekilebilir.
#Türkce paketi (DataSet klasörünün içinde) /usr/share/tesseract-ocr/tessdata/ adresine kopyalanmalıdır.

text=pytesseract.image_to_string(Image.fromarray(thres))
#text=pytesseract.image_to_string(Image.fromarray(thres), lang='tur')
print text

cv2.imshow('image',img)
cv2.waitKey(0)
