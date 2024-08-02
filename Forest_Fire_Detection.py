import cv2
import numpy as np

def detect_fire(image_path):
    image = cv2.imread(image_path)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])
    mask = cv2.inRange(hsv_image, lower_red, upper_red)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        print("Forest Fire Detected!")
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cv2.imshow("Detected Fire", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("No fire detected.")

image_path = r"D:\DEVENDRA\VS Code\Project\python\fire.webp"
detect_fire(image_path)
