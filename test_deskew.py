import cv2
from dataset_service import DatasetService
# from services.dataset_service import DatasetService
from deskew_service import DeskewService
from graphics_service import ResizeImagewithAspectRatio

# We can test how the results of deskew procedure look

# Open the dataset
dataset = DatasetService().openDataset()

# print(dataset)

for i in range(0, len(dataset)):
    # Get image and angle
    item = dataset[i]
    imageCv = item[0]
    correctAngle = item[1]

    # Deskew the image, and compare calculated skew angle to real one
    deskewedImage, guessedAngle = DeskewService().deskew(imageCv)
    difference = abs(correctAngle - guessedAngle)
    differencePercentage = round(abs(difference / correctAngle) * 100, 2)

    imageCv = ResizeImagewithAspectRatio(imageCv, width=564, inter=cv2.INTER_AREA)
    deskewedImage = ResizeImagewithAspectRatio(deskewedImage, width=564, inter=cv2.INTER_AREA)

    print('Item #' + str(i) + ', with angle=' + str(correctAngle) + ', calculated=' + str(guessedAngle) + ', difference=' + str(differencePercentage) + '%')
    cv2.imshow('Skewed-image', imageCv)

    if guessedAngle < -50.0:
        deskewedImage = cv2.rotate(deskewedImage,cv2.ROTATE_90_CLOCKWISE)
    cv2.imshow('Deskewed-image', deskewedImage)
    cv2.waitKey(0)
cv2.destroyAllWindows()