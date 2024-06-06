import numpy as np
from numpy.linalg import norm
import streamlit as st

import numpy as np

def get_bounding_box_features(bounding_boxes):
    heights = []
    widths = []
    areas = []
    
    for x1, y1, x2, y2 in bounding_boxes:
        height = y2 - y1
        width = x2 - x1
        area = height * width
        
        heights.append(height)
        widths.append(width)
        areas.append(area)
    
    heights = np.array(heights)
    widths = np.array(widths)
    areas = np.array(areas)

    normalized_areas = areas / areas.sum()
    
    return normalized_areas

def cos_sim(A,B):
    A = np.array(A)
    B = np.array(B)

    if len(A) > len(B):
        A = A[:len(B)]
    elif len(B) > len(A):
        B = B[:len(A)]

    A = A.reshape(-1, 1)
    B = B.reshape(-1, 1)

    cosine = np.dot(A, B.T) / (norm(A, axis=1) * norm(B, axis=1))
    
    mean_cosine_similarity = np.mean(cosine)
    st.write("The final score is: ", mean_cosine_similarity/10)

