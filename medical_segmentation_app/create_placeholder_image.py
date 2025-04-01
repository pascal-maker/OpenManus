import cv2
import numpy as np

# Create a simple black image with a white square in the center
image = np.zeros((256, 256, 3), dtype=np.uint8)
cv2.rectangle(image, (96, 96), (160, 160), (255, 255, 255), -1)

# Save the image
cv2.imwrite('/Users/pascal-maker/OpenManus/medical_segmentation_app/sample_image.png', image)

print('Placeholder image created and saved as sample_image.png')