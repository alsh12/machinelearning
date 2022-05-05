import os
import cv2
import pandas as pd

train_path = "F:/Learning/Python/Extra Examples/PoseEstimation/PoseEstimationCNN/Pose_DataSet/train/"

df = pd.read_csv("Pose_Dataset/train_joints_coords.csv")
df1 = df.head(2)
imageNames = []

for i in range(len(df1)):

    imageName = df1["ImageName"][i]
    image_path = train_path + imageName
    image = cv2.imread(image_path, 1)
    imageNames.append(imageName)

    width= image.shape[0]
    height = image.shape[1]
    print(width)
    print(height)

    cv2.imshow("", image)

    cv2.waitKey(0)