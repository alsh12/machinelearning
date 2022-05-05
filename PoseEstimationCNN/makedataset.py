import os
import cv2
import pandas as pd

train_path = "F:/Learning/Python/Extra Examples/PoseEstimation/PoseEstimationCNN/Pose_DataSet/train/"
test_path = "F:/Learning/Python/Extra Examples/PoseEstimation/PoseEstimationCNN/Pose_DataSet/test/"

df = pd.read_csv("Pose_Dataset/train_joints_coords.csv")

df1 = df.head(10)
print(df1)
imageNames = []
cords1 = []
cords2 = []
cords3 = []
cords4 = []
cords5 = []
cords6 = []
cords7 = []
cords8 = []
cords9 = []
cords10 = []
cords11 = []
cords12 = []
cords13 = []
cords14 = []

## List of Body Parts ##
bodyParts = [
    "nose", "leftEye", "rightEye", "leftEar", "rightEar", "leftShoulder",
    "rightShoulder", "leftElbow", "rightElbow", "leftWrist", "rightWrist",
    "leftHip", "rightHip", "leftKnee", "rightKnee", "leftAnkle", "rightAnkle"
]

## Defining a chain / tree based on nose as root point ##
chainPoint = [
    ["nose", "leftEye"], ["leftEye", "leftEar"], ["nose", "rightEye"],
    ["rightEye", "rightEar"], ["nose", "leftShoulder"],
    ["leftShoulder", "leftElbow"], ["leftElbow", "leftWrist"],
    ["leftShoulder", "leftHip"], ["leftHip", "leftKnee"],
    ["leftKnee", "leftAnkle"], ["nose", "rightShoulder"],
    ["rightShoulder", "rightElbow"], ["rightElbow", "rightWrist"],
    ["rightShoulder", "rightHip"], ["rightHip", "rightKnee"],
    ["rightKnee", "rightAnkle"]
]
## Making Part Connection for skeleton ##
connectedPartNames = [
    ['leftHip', 'leftShoulder'], ['leftElbow', 'leftShoulder'],
    ['leftElbow', 'leftWrist'], ['leftHip', 'leftKnee'],
    ['leftKnee', 'leftAnkle'], ['rightHip', 'rightShoulder'],
    ['rightElbow', 'rightShoulder'], ['rightElbow', 'rightWrist'],
    ['rightHip', 'rightKnee'], ['rightKnee', 'rightAnkle'],
    ['leftShoulder', 'rightShoulder'], ['leftHip', 'rightHip']
]

## Defining Body Points ##
bodyPoints = {}
for i in range(len(bodyParts)):
    bodyPoints[bodyParts[i]] = i

## Defining Connected Body Parts corresponding to part names ##########################

connectedPartIndices = []


def part_indices(connected_part_names, dict_part_ids, connected_part_indices):
    for jointNameA, jointNameB in connected_part_names:
        connected_part_indices.append([dict_part_ids[jointNameA], dict_part_ids[jointNameB]])


part_indices(connectedPartNames, bodyPoints, connectedPartIndices)

print(connectedPartIndices)

## Parent Child nodes for gradients displacement ##
parentChildren = []

for jointName in chainPoint:
    ParentJointName = jointName[0]
    ChildJointName = jointName[1]
    parentChildren.append([bodyPoints[ParentJointName],bodyPoints[ChildJointName]])

print("Parent Children: ", parentChildren)
## Create skeleton with sixteen edges ##
parentToChildEdges = []
for jointId in parentChildren:
    parentToChildEdges.append(jointId[1])

print("Parent - Child Edges: ", parentToChildEdges)

childToParentEdges = []
for jointId in parentChildren:
    childToParentEdges.append(jointId[0])

print("Child - Parent Edges: ", childToParentEdges)


# def poseEstimation(img):
#
# print(len(df))
#
for i in range(len(df1)):

    imageName = df1["ImageName"][i]
    imageNames.append(imageName)
#     cord1 = df1["Cord1"][i]
#     cord2 = df1["Cord2"][i]
#     cord3 = df1["Cord3"][i]
#     cord4 = df1["Cord4"][i]
#     cord5 = df1["Cord5"][i]
#     cord6 = df1["Cord6"][i]
#     cord7 = df1["Cord7"][i]
#     cord8 = df1["Cord8"][i]
#     cord9 = df1["Cord9"][i]
#     cord10 = df1["Cord10"][i]
#     cord11 = df1["Cord11"][i]
#     cord12 = df1["Cord12"][i]
#     cord13 = df1["Cord13"][i]
#     cord14 = df1["Cord14"][i]
#
#     # Add Cordinates to list
#     cords1.append(cord1)
#     cords2.append(cord2)
#     cords3.append(cord3)
#     cords4.append(cord4)
#     cords5.append(cord5)
#     cords6.append(cord6)
#     cords7.append(cord7)
#     cords8.append(cord8)
#     cords9.append(cord9)
#     cords10.append(cord10)
#     cords11.append(cord11)
#     cords12.append(cord12)
#     cords13.append(cord13)
#     cords14.append(cord14)
#
#
for i in range(len(df1)):
    image_path = "F:/Learning/Python/Extra Examples/PoseEstimation/PoseEstimationCNN/Pose_DataSet/train/" +imageNames[i]
    image = cv2.imread(image_path, 1)
    frameWidth = image.shape[1]
    frameHeight = image.shape[0]
    print(frameWidth," for " , imageNames[i])
    print(frameHeight, " for " , imageNames[i])
#     cv2.circle(image, (cords1[i], cords2[i]), 2, (0, 255, 0), -1)
#     cv2.circle(image, (cords3[i], cords4[i]), 2, (0, 255, 0), -1)
#     cv2.circle(image, (cords5[i], cords6[i]), 2, (0, 255, 0), -1)
#     cv2.circle(image, (cords7[i], cords8[i]), 2, (0, 255, 0), -1)
#     cv2.circle(image, (cords9[i], cords10[i]), 2, (0, 255, 0), -1)
#     cv2.circle(image, (cords11[i], cords12[i]), 2, (0, 255, 0), -1)
#     cv2.circle(image, (cords13[i], cords14[i]), 2, (0, 255, 0), -1)
#
    cv2.imshow("",image)

    cv2.waitKey(0)
