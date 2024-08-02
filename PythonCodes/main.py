# import cv2
# from number_plate_recognition import extract_text ,detect_license_plate 

# # frameWidth = 640   #Frame Width
# frameWidth = 1000   #Frame Width
# frameHeight = 480   # Frame Height

# plateCascade = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")
# minArea = 500

# cap = cv2.VideoCapture(0)
# cap.set(3, frameWidth)
# cap.set(4, frameHeight)
# cap.set(10, 150)
# count = 0

# while True:
#     success, img = cap.read()

# # converting image to gray scale
#     imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# # parameters for image
#     numberPlates = plateCascade.detectMultiScale(imgGray, 1.1, 4)

#     for (x, y, w, h) in numberPlates:
#         area = w * h
#         if area > minArea:
#             cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
#             cv2.putText(img, "NumberPlate", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
#             imgRoi = img[y:y + h, x:x + w]
#             cv2.imshow("Number Plate", imgRoi)

#             # # Auto save the captured image
#             # cv2.imwrite(f".\\DetectedPlates\\plate_{count}.jpg", imgRoi)
#             # count += 1

            
#             # Extract text from the captured image
#             text = extract_text(imgRoi)
#             print("Extracted text:", text)

#              # Detect license plate format and save the image if the format matches
#             detect_license_plate(text, imgRoi, f"DetectedPlates/image_{count}.jpg")
#             count += 1


# #  Frame capture with timing
#     cv2.imshow("Result", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()

# ===============================OPENING AND CLOSING====================================================
import cv2
from number_plate_recognition import extract_text, detect_license_plate

# frameWidth = 640   #Frame Width
frameWidth = 1000   #Frame Width
frameHeight = 480   # Frame Height

plateCascade = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")
minArea = 500

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)
count = 0 # no. of number plate detected

while True:
    success, img = cap.read()

    # converting image to gray scale
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply opening morphological operation
    kernel_open = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    imgGray_opening = cv2.morphologyEx(imgGray, cv2.MORPH_OPEN, kernel_open)

    # Apply closing morphological operation
    kernel_close = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    imgGray_closing = cv2.morphologyEx(imgGray_opening, cv2.MORPH_CLOSE, kernel_close)

    # parameters for image
    numberPlates = plateCascade.detectMultiScale(imgGray_closing, 1.1, 4)

    for (x, y, w, h) in numberPlates:
        area = w * h
        if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(img, "NumberPlate", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
            imgRoi = img[y:y + h, x:x + w]
            cv2.imshow("Number Plate", imgRoi)

            # Extract text from the captured image
            text = extract_text(imgRoi)
            print("Extracted text:", text)

            # Detect license plate format and save the image if the format matches
            detect_license_plate(text, imgRoi, f"DetectedPlates/image_{count}.jpg")
            count += 1

    #  Frame capture with timing
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
