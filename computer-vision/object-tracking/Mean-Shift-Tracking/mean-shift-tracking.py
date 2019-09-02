"""
This script was written by following this tutorial made by Pysource on Youtube:
https://www.youtube.com/watch?v=EDT0vHsMy34&t=0s&list=LL_nJcU3CiKaa8b27n2dvsoQ&index=19
"""
import cv2

# use this video for demonstration
video = cv2.VideoCapture("videos/mouthwash.avi")

# grab the first frame and specify the starting region
_, first_frame = video.read()
x = 300
y = 305
w = 100
h = 115
roi = first_frame[y:y + h, x:x + w]

# convert from RBG/BGR to HSV
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

# calculate the histogram of this image
# https://docs.opencv.org/2.4/modules/imgproc/doc/histograms.html
roi_hist = cv2.calcHist([hsv_roi], [0], None, [180], [0, 180])

# normalize the histogram to 0 - 255
roi_hist = cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

# show the image
#cv2.imshow("First frame", roi)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

term_criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

# repeatedly show every frame
while True:
    # grab one frame
    _, frame = video.read()

    # convert to histogram
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)

    # perform mean shift algorithm to get next box
    _, track_window = cv2.meanShift(mask, (x, y, w, h), term_criteria)
    x, y, w, h = track_window
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # show both the histogram and frame with bounding box
    cv2.imshow("Mask", mask)
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(60)

    # hit ESC to close window
    if key == 27:
        break

video.release()
cv2.destroyAllWindows()
