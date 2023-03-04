import cv2
import numpy as np

cap = cv2.VideoCapture(0)


# Blue
blue_upper_bond = np.array([120, 255, 255])
blue_lower_bond = np.array([95, 43, 67])

# Pink
pink_upper_bond = np.array([179, 255, 255])
pink_lower_bond = np.array([80, 95, 0])

# Green
green_upper_bond = np.array([86,255,255])
green_lower_bond = np.array([41,47, 72])

# Skin
skin_upper_bond = np.array([40,246,218])
skin_lower_bond = np.array([0,84, 0])

# Hair
hair_upper_bond = np.array([179,255,255])
hair_lower_bond = np.array([29,91, 0])


class ColorMatrix():
    def __init__(self,rgb=(0,0,0),ub=np.array([0,0,0]),lb=np.array([0,0,0])):
        self.rgb = rgb
        self.ub = ub
        self.lb = lb
        self.mtx = np.zeros((480,640,3), np.uint8)
        self.mtx[:, :, 0] = self.rgb[0]
        self.mtx[:, :, 1] = self.rgb[1]
        self.mtx[:, :, 2] = self.rgb[2]

while True:
    _, frame = cap.read()
    image = cv2.flip(frame, 1)

    # curtain detector
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


    blue_mtx = ColorMatrix(rgb=(232,159,95),ub=blue_upper_bond,lb=blue_lower_bond)
    green_mtx = ColorMatrix(rgb=(118,232,95),ub=green_upper_bond,lb=green_lower_bond)
    pink_mtx = ColorMatrix(rgb=(95,129,232),ub=pink_upper_bond,lb=pink_lower_bond)
    skin_mtx = ColorMatrix(rgb=(95,200,232),ub=skin_upper_bond,lb=skin_lower_bond)
    hair_mtx = ColorMatrix(rgb=(95,166,232),ub=hair_upper_bond,lb=hair_lower_bond)


    edge_mtx = ColorMatrix(rgb=(236,252,3))
    img_blur = cv2.GaussianBlur(img_gray, (3, 3), 0,0)
    edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200)  # Canny Edge Detection
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2, 2))  # Kernel shape
    dilated_edges = cv2.dilate(edges, kernel)
    edge_image = cv2.bitwise_and(image,image,mask=dilated_edges)


    matrix = [green_mtx,blue_mtx,skin_mtx]
    masks = []
    for mat in matrix:
        mask = cv2.inRange(hsv, mat.lb, mat.ub)
        _, mask = cv2.threshold(mask, 1, 255, cv2.THRESH_BINARY)
        masks.append(mask)

    masked_images = []
    for i,mask in enumerate(masks):
        masked_image = cv2.bitwise_and(matrix[i].mtx, matrix[i].mtx, mask=mask)
        masked_images.append(masked_image)

    result = edge_image
    for resmat in masked_images:
        result = cv2.add(result,resmat)

    cv2.imshow('result', result)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()
