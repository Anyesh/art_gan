import cv2
import numpy as np


data_path = 'training_data.npy'
datas = np.load(data_path)

for data in datas:
    cv2.imshow("Img", data)
    cv2.waitKey()
