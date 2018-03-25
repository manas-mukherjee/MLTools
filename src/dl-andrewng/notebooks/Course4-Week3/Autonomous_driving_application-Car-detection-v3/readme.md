View Project -

Residual Network Tutorial
http://htmlpreview.github.io/?https://github.com/manas-mukherjee/MLTools/blob/master/src/dl-andrewng/notebooks/Course4-Week3/Autonomous_driving_application-Car-detection-v3/AutonomousDrivingApplication-Car-detection-v3.html

<font color='blue'>
**Summary for YOLO**:

- Input image (608, 608, 3)
- The input image goes through a CNN, resulting in a (19,19,5,85) dimensional output.
- After flattening the last two dimensions, the output is a volume of shape (19, 19, 425):
    - Each cell in a 19x19 grid over the input image gives 425 numbers.
    - 425 = 5 x 85 because each cell contains predictions for 5 boxes, corresponding to 5 anchor boxes, as seen in lecture.
    - 85 = 5 + 80 where 5 is because $(p_c, b_x, b_y, b_h, b_w)$ has 5 numbers, and and 80 is the number of classes we'd like to detect
- You then select only few boxes based on:
    - Score-thresholding: throw away boxes that have detected a class with a score less than the threshold
    - Non-max suppression: Compute the Intersection over Union and avoid selecting overlapping boxes
- This gives you YOLO's final output.