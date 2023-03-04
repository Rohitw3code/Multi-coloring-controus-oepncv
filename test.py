import cv2
import numpy as np

# create two example contours
contour1 = np.array([[100, 100], [200, 100], [200, 200], [100, 200]])
contour2 = np.array([[300, 300], [400, 300], [400, 400], [300, 400]])

# create an empty image to draw the contours onto
image = np.zeros((500, 500, 3), dtype=np.uint8)



# join the two contours by drawing one onto the other
cv2.drawContours(image, [contour1, contour2], 0, (0, 0, 255), -1)

# display the image
cv2.imshow("Joined Contours", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
