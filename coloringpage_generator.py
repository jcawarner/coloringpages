import cv2
import os


filename = input("What is the customers name? ")
file_ext = "jpg"

image_path = filename + "." + file_ext



image = cv2.imread(image_path)

# Image path


grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey_img)  # helps in masking of the image
# sharp edges in images are smoothed while minimizing too much blurring
blur = cv2.GaussianBlur(invert, (21, 21), 0)
invertedblur = cv2.bitwise_not(blur)
sketch = cv2.divide(grey_img, invertedblur, scale=256.0)
cv2.imwrite(image_path, sketch)

cv2.waitKey(0)

cv2.destroyAllWindows()


print(image_path)