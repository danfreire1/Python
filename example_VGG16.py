# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 14:48:33 2020

@author: danie
"""

from keras.applications import VGG16
from keras.applications import imagenet_utils
from keras.preprocessing.image import img_to_array, load_img
import numpy as np
import cv2

#loading the image to predict
img_path = 'images/test5.jpg'
img = load_img(img_path)

#resize the image to 224x224 square shape
img = img.resize((224,224))

#convert the image to array
img_array = img_to_array(img)

#convert the image into a 4 dimensional Tensor
#convert from (height, width, channels), (batchsize, height, width, channels)
img_array = np.expand_dims(img_array, axis=0)

#preprocess the input image array
img_array = imagenet_utils.preprocess_input(img_array)

#Load the model from internet / computer
#approximately 530 MB
pretrained_model = VGG16(weights="imagenet")

#predict using predict() method
prediction = pretrained_model.predict(img_array)

#decode the prediction
actual_prediction = imagenet_utils.decode_predictions(prediction)

print(actual_prediction)

