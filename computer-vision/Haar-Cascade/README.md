# Face Detection with OpenCV
This is a quick exercise of face detection with with openCV. The classifier used here is Haar feature-based cascade classifier by Paul Viola and Michael Jones. The guide that I used to make this can be found [here](https://docs.opencv.org/3.4.1/d7/d8b/tutorial_py_face_detection.html).

## Parameter Tuning Results
Scale factor = 1.05, min neighbors = 0:

Clearly a bad idea to set min neighbors to 0...

![screenshot](https://github.com/hsuanhauliu/coding-practice/blob/master/computer-vision/Haar-Cascade/outputs/1050.jpg "screenshot")

Scale factor = 1.05, min neighbors = 2:

Getting much better when we limit min neighbors to some number that actually make sense.

![screenshot](https://github.com/hsuanhauliu/coding-practice/blob/master/computer-vision/Haar-Cascade/outputs/1052.jpg "screenshot")

Scale factor = 1.05, min neighbors = 5:

![screenshot](https://github.com/hsuanhauliu/coding-practice/blob/master/computer-vision/Haar-Cascade/outputs/1055.jpg "screenshot")

Scale factor = 1.1, min neighbors = 5:

Best result so far.

![screenshot](https://github.com/hsuanhauliu/coding-practice/blob/master/computer-vision/Haar-Cascade/outputs/1105.jpg "screenshot")

Scale factor = 1.2, min neighbors = 5:

The eyes are becoming difficult to detect when we raise the scale factor.

![screenshot](https://github.com/hsuanhauliu/coding-practice/blob/master/computer-vision/Haar-Cascade/outputs/1205.jpg "screenshot")

Scale factor = 1.3, min neighbors = 5:

![screenshot](https://github.com/hsuanhauliu/coding-practice/blob/master/computer-vision/Haar-Cascade/outputs/1305.jpg "screenshot")

A different image with scale factor = 1.01, min neighbors = 3:

Interestingly enough, weird parts are being recognized as faces with low scale factor...

![screenshot](https://github.com/hsuanhauliu/coding-practice/blob/master/computer-vision/Haar-Cascade/outputs/1013.jpg "screenshot")
