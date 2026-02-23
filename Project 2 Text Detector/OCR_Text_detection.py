import os
import easyocr as ocr
import numpy as np
import cv2
reader = ocr.Reader(['en'],gpu=False)
os.makedirs('output', exist_ok=True)

data_path = r"F:\Skill Set\Computer Vision\Project 2 Text Detector\text detection.v1i.coco\train"

for filename in os.listdir(data_path):
    if 'jpg' in filename or 'png' in filename:
        img_path = os.path.join(data_path, filename)
        img = cv2.imread(img_path)
        results = reader.readtext(img_path)
        for result in results:
            bbox, text, confidence = result
            if confidence > 0.5:
                pts = np.array(bbox, dtype=np.int32)
                bbox = cv2.polylines(img, [pts],True,(0,255,0),2)
                cv2.putText(img, text, tuple(pts[0]),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
        cv2.imwrite(os.path.join('output',filename),img)