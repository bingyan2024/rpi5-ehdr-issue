from picamera2 import Picamera2
import time
import cv2

picam2 = Picamera2()
config = picam2.create_preview_configuration({'format': 'RGB888'}, raw={'format': 'SGRBG16'})
picam2.start(config)

time.sleep(5)

images = []
picam2.switch_mode(config)
for _ in range(10):
    images.append(picam2.capture_array())
for i, image in enumerate(images):
    cv2.imwrite(f"image_{i}.jpg", image)
