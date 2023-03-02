import cv2


cap = cv2.VideoCapture(0)
def nothing(x):
    pass
# cv2.namedWindow('image')
# cv2.createTrackbar('a', 'image', 50, 200, nothing)
# cv2.createTrackbar('b', 'image', 100, 500, nothing)


while True:
    _, frame = cap.read()
    img = cv2.flip(frame, 1)
    # Convert to graycsale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Blur the image for better edge detection
    # a = cv2.getTrackbarPos('a', 'image')
    # b = cv2.getTrackbarPos('b', 'image')
    img_blur = cv2.GaussianBlur(img_gray, (3, 3), 0)

    # Canny Edge Detection
    edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200)  # Canny Edge Detection
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))  # Kernel shape
    dilated_edges = cv2.dilate(edges, kernel)
    res = cv2.bitwise_and(img,img,mask=dilated_edges)


    # Display Canny Edge Detection Image
    cv2.imshow('Canny Edge Detection', res)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break


cap.release()

cv2.destroyAllWindows()