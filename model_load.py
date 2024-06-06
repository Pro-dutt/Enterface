from ultralytics import YOLO
import streamlit as st
import global_file
import cv2
import numpy as np
from collections import Counter
import pandas as pd
from ultralytics.solutions import object_counter
from class_classification import classify as cls
from cosine_similarity import get_bounding_box_features, cos_sim as cos
class Model:

    #Loading of YOLO v8 pt file
    def load_model():
        model = YOLO('model/best.pt')
        device = 'cpu'
        model.to(device)
        return model

    global_file.Model = load_model()

    def model_button():
        Uploaded_Image = global_file.Uploaded_Image
        Comparision_Image = global_file.Comparision_Image
        results_1 = global_file.Model(Uploaded_Image)
        results_2 = global_file.Model(Comparision_Image)

        uploaded_image = cv2.cvtColor(np.array(Uploaded_Image), cv2.COLOR_RGB2BGR)
        comparision_image = cv2.cvtColor(np.array(Comparision_Image), cv2.COLOR_RGB2BGR)

        for result in results_1:
            boxes_1 = result.boxes.xyxy.tolist()
            classes_1 = result.boxes.cls
            st.write(classes_1)
            
            annotated_image_upload = result.plot()
            annotated_image_upload = cv2.cvtColor(np.asarray(annotated_image_upload), cv2.COLOR_RGB2BGR)

        for result in results_2:
            boxes_2 = result.boxes.xyxy.tolist()
            classes_2 = result.boxes.cls
            st.write(classes_2)
            annotated_image_compare = result.plot()
            annotated_image_compare = cv2.cvtColor(np.asarray(annotated_image_compare), cv2.COLOR_RGB2BGR)
        
        st.divider()
        st.header('Model Detected Image(1):')
        st.image(annotated_image_upload, channels="BGR")
        st.write('Instances detected: ')
        st.write(len(classes_1))

        
        # Coordinates of 1st Box:
        bounding_boxes_1 = []
        for box in boxes_1:
                x1, y1, x2, y2 = [int(value) for value in box]
                x1 = int(x1 / 1020 * uploaded_image.shape[1])
                y1 = int(y1 / 1020 * uploaded_image.shape[0])
                x2 = int(x2 / 1020 * uploaded_image.shape[1])
                y2 = int(y2 / 1020 * uploaded_image.shape[0])
                bounding_boxes_1.append((x1, y1, x2, y2))
                cv2.rectangle(uploaded_image, (x1, y1), (x2, y2), (36, 255, 12), 2)
        
        cls(classes_1)
             
        st.divider()
        st.header('Model Detected Image(2):')
        st.image(annotated_image_compare, channels="BGR")
        st.write('Instances detected: ')
        st.write(len(classes_2))

        # Coordinates of 2nd Box:
        bounding_boxes_2 = []
        for box in boxes_2:
                x1, y1, x2, y2 = [int(value) for value in box]
                x1 = int(x1 / 1020 * comparision_image.shape[1])
                y1 = int(y1 / 1020 * comparision_image.shape[0])
                x2 = int(x2 / 1020 * comparision_image.shape[1])
                y2 = int(y2 / 1020 * comparision_image.shape[0])
                bounding_boxes_2.append((x1, y1, x2, y2))
                cv2.rectangle(comparision_image, (x1, y1), (x2, y2), (36, 255, 12), 2)
        cls(classes_2)

        st.divider()
        st.header('Area Borders of Image(1): ')
        st.image(uploaded_image, channels='BGR')

        st.divider()
        st.header('Area Borders of Image(2): ')
        st.image(comparision_image, channels='BGR')

        norm_area_1 = get_bounding_box_features(bounding_boxes_1)
        norm_area_2 = get_bounding_box_features(bounding_boxes_2)
        
        st.write(norm_area_1.reshape(-1, 1))
        st.write(norm_area_2.reshape(-1, 1))
        cos(norm_area_1, norm_area_2)


