# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 11:40:43 2020

@author: danie
"""

#importar as bibliotecas
import pytesseract;
import pkg_resources;
import cv2;

#Declarar o caminho do exe do tesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe';

#print versão do tesseract
print(pkg_resources.working_set.by_key['pytesseract'].version);

#print versão do opencv
print(cv2.__version__);