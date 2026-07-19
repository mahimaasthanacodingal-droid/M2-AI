# After a long time; I finally managed to get opencv back and running!

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("/Users/swagatmohanty/Documents/Python 2/example 2.jpg")

# Exception Handling - gives two condtitions

if image is None:
    print("An error occured. Please try again!")

else: 
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Rotation

    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)

    M = cv2.getRotationMatrix2D(center, 45, 1.0) 
    rotated = cv2.warpAffine(image, M, (w, h)) 
    rotated_rgb = cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB)

# Cropping

    cropped = image[0:300, 0:300]
    cropped_rgb = cv2.cvtColor(cropped, cv2.COLOR_BGR2RGB)

# Brightness

    brightness_matrix = np.ones(image.shape, dtype="uint8") * 50
    brighter = cv2.add(image, brightness_matrix)
    brighter_rgb = cv2.cvtColor(brighter, cv2.COLOR_BGR2RGB)

    fig, axes = plt.subplots(1, 4, figsize=(20,5))

# Different Use of Visualation - Puts images all at once

    axes[0].imshow(image_rgb)
    axes[0].set_title("Original Image")
 
    axes[1].imshow(rotated_rgb)
    axes[1].set_title("Rotated Image")

    axes[2].imshow(cropped_rgb)
    axes[2].set_title("Cropped Image")

    axes[3].imshow(brighter_rgb)
    axes[3].set_title("Brighter Image")

# For loop to run above expressions

    for ax in axes:
            ax.axis("off")
    plt.show()