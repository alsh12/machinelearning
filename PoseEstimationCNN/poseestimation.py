import os
import cv2
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Conv2D, MaxPool2D

train_path = "F:/Learning/Python/Extra Examples/PoseEstimation/PoseEstimationCNN/Pose_DataSet/train/"
test_path = "F:/Learning/Python/Extra Examples/PoseEstimation/PoseEstimationCNN/Pose_DataSet/test/"

x_train = []
counter = 0
for image in os.listdir(train_path):
    image_path=train_path + image

    img_arr = cv2.imread(image_path)
    if img_arr is None:
        counter +=1
    else:
        img_arr = cv2.resize(img_arr, (224, 224))

    x_train.append(img_arr)

x_test = []

for image in os.listdir(test_path):
    image_path = test_path + image
    img_arr = cv2.imread(image_path)
    img_arr = cv2.resize(img_arr, (224, 224))

    x_test.append(img_arr)

train_x = np.array(x_train)
test_x = np.array(x_test)

train_x = train_x/255.0
test_x = test_x/255.0

# building a linear stack of layers with the sequential model
model = Sequential()

# hidden layer
model.add(Dense(100, input_shape=(224*224,), activation='relu'))

# output layer
model.add(Dense(10, activation='softmax'))

# looking at the model summary
model.summary()

# compiling the sequential model
model.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer='adam')







