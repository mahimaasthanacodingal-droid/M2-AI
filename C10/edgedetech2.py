import cv2
import numpy as np
import matplotlib.pyplot as plt

def interactive_edge_detection(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print("Image Not Found!")
        return
    
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    while True:
        print("\n1. Sobel  2. Canny  3. Laplacian  4. Gaussian  5. Median  6. Compare All  7. Exit")
        choice = input("Enter choice (1-7): ")

        # Gives choice for each one and includes option 1 and 6
        if choice in ['1', '6']:
            sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
            sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
            sobel = cv2.bitwise_or(sobel_x.astype(np.uint8), sobel_y.astype(np.uint8))
        
        if choice in ['2', '6']:
            lt = int(input("Canny Lower Threshold (e.g. 100): "))
            ut = int(input("Canny Upper Threshold (e.g. 200): "))
            canny = cv2.Canny(gray_image, lt, ut)
            
        if choice in ['3', '6']:
            laplacian = np.abs(cv2.Laplacian(gray_image, cv2.CV_64F)).astype(np.uint8)

        if choice in ['4', '6']:
            k_g = int(input("Gaussian Kernel (odd): "))
            gauss = cv2.GaussianBlur(rgb_image, (k_g, k_g), 0)

        if choice in ['5', '6']:
            k_m = int(input("Median Kernel (odd): "))
            median = cv2.medianBlur(rgb_image, k_m)

        # Multi-plot display for Option 6
        if choice == '6':
            titles = ['Original', 'Sobel', 'Canny', 'Laplacian', 'Gaussian', 'Median']
            images = [gray_image, sobel, canny, laplacian, gauss, median]
            
            plt.figure(figsize=(15, 10))
            for i in range(6):
                plt.subplot(2, 3, i+1)
                cmap = 'gray' if len(images[i].shape) == 2 else None
                plt.imshow(images[i], cmap=cmap)
                plt.title(titles[i])
                plt.axis("off")
            plt.tight_layout()
            plt.show()
            
        elif choice == '7':
            break
# Giving function name and image_path
interactive_edge_detection('example.jpg')