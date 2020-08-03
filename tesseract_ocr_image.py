# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 11:40:43 2020

@author: danie
"""

#importar as bibliotecas 
from PIL import Image
import pytesseract
import cv2

#Declarar o caminho do exe do tesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


# carrega a imagem do disco
image_to_ocr = cv2.imread('images/testing/fox_sample2.png')

#pre_processamento da imagem
# passo 1: converter para escala cinza (grayscale)
preprocessed_img = cv2.cvtColor(image_to_ocr, cv2.COLOR_BGR2GRAY)

# passo 2: Do binary and otsu thresholding
preprocessed_img = cv2.threshold(preprocessed_img,0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# passo 3: Smooth the image using median blur
preprocessed_img = cv2.medianBlur(preprocessed_img, 3)

#passo 4: Salvar e abrir a imagem temporária
# save the preprocessed image temporarily into the disk
cv2.imwrite('temp_img.jpg',preprocessed_img);

# load the image as a PIL/Pillow image
preprocessed_pil_img = Image.open('temp_img.jpg')

# pass the pil image to tesseract to do OCR
text_extracted = pytesseract.image_to_string(preprocessed_pil_img)

# print the text
print(text_extracted)

# display the original image
cv2.imshow("Imagem atual",image_to_ocr)
