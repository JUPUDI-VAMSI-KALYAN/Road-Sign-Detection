# -*- coding: utf-8 -*-
import streamlit as st
import pickle
import cv2
import numpy as np
import os
import tensorflow
import keras
import pandas
from PIL import Image
font = cv2.FONT_HERSHEY_SIMPLEX
try:
    pickle_in=open("veltech_minor_model.p","rb")
    model=pickle.load(pickle_in)
except:
    st.write("Pickle Loading Error")
    
def grayscale(img):
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    return img
def equalize(img):
    img =cv2.equalizeHist(img)
    return img
def preprocessing(img):
    img = grayscale(img)
    img = equalize(img)
    img = img/255
    return img
def getCalssName(classNo):
    if   classNo == 0: 
        return 'Speed Limit 20 km/h'
    elif classNo == 1: 
        return 'Speed Limit 30 km/h'
    elif classNo == 2: 
        return 'Speed Limit 50 km/h'
    elif classNo == 3: 
        return 'Speed Limit 60 km/h'
    elif classNo == 4:
        return 'Speed Limit 70 km/h'
    elif classNo == 5:
        return 'Speed Limit 80 km/h'
    elif classNo == 6:
        return 'End of Speed Limit 80 km/h'
    elif classNo == 7:
        return 'Speed Limit 100 km/h'
    elif classNo == 8:
        return 'Speed Limit 120 km/h'
    elif classNo == 9:
        return 'Yield'
    elif classNo == 10: 
        return 'Stop'
    elif classNo == 11:
        return 'General caution'
    elif classNo == 12:
        return 'Dangerous curve to the left'
    elif classNo == 13:
        return 'Dangerous curve to the right'
    elif classNo == 14:
        return 'Double curve'
    elif classNo == 15:
        return 'Bumpy road'
    elif classNo == 16:
        return 'Slippery road'
    elif classNo == 17:
        return 'Road narrows on the right'
    elif classNo == 18:
        return 'Road work'
    elif classNo == 19:
        return 'Pedestrians'
    elif classNo == 20:
        return 'Children crossing'
    elif classNo == 21:
        return 'Bicycles crossing'
    elif classNo == 22:
        return 'End of all speed and passing limits'
    elif classNo == 23:
        return 'Turn right ahead'
    elif classNo == 24:
        return 'Turn left ahead'
    elif classNo == 25:
        return 'Ahead only'
    elif classNo == 26:
        return 'Go straight or right'
    elif classNo == 27:
        return 'Go straight or left'
    elif classNo == 28:
        return 'Keep right'
    elif classNo == 29:
        return 'Keep left'
    elif classNo == 30:
        return 'No Entry'
    elif classNo == 31:
        return 'No Entry for Heavy Vehicels'
    
def about():
    st.title("About This Project")
    
    
def main():
    st.title("RoadSign Detection App :sunglasses:")
    st.write("**Using the loded pickle file**")
    Activities = ["Home","About"]
    choice = st.sidebar.selectbox("Pick Something",Activities)
    if choice == "Home":
        image_file = st.file_uploader("Upload Image",type=["jpeg","png","jpg"])
        if image_file is not None:
            if st.button("Processes"):
                img = np.asarray(image_file)
                img = cv2.resize(img, (32, 32))
                img = preprocessing(img)
                cv2.imshow("Processed Image", img)
                img = img.reshape(1, 32, 32, 1)
                cv2.putText(image_file, "CLASS: " , (20, 35), font, 0.75, (0, 0, 255), 2, cv2.LINE_AA)
                classIndex = model.predict_classes(img)
                cv2.putText(image_file,str(classIndex)+" "+str(getCalssName(classIndex)), (120, 35), font, 0.75, (0, 0, 255), 2, cv2.LINE_AA)
                st.image(image_file,use_colomn_width=True)
    elif choice=="About":
        about()
        
if __name__ == "main":
    main()
            
        