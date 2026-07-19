import cv2
import numpy as np

def apply_color_filter(image, filter_type):
    filtered_image = image.copy()

    if filter_type == "orignal":
        return filtered_image
    
    elif filter_type == "red_tint":
        filtered_image[:, :, 0] = 0
        filtered_image[:, :, 1] = 0

    elif filter_type == "blue_tint":
        filtered_image[:, :, 1] = 0
        filtered_image[:, :, 2] = 0

    elif filter_type == "green_tint":
        filtered_image[:, :, 0] = 0
        filtered_image[:, :, 2] = 0

    elif filter_type == "increased_red":
        filtered_image[:, :, 2] = cv2.add(filtered_image[:, :, 2], 50)
    
    elif filter_type == "increased_blue": 
        filtered_image[:, :, 0] = cv2.add(filtered_image[:, :, 0], 50) 
        
    elif filter_type == "increased_green": 
        filtered_image[:, :, 1] = cv2.add(filtered_image[:, :, 1], 50) 

    elif filter_type == "decreased_red":
        filtered_image[:, :, 2] = cv2.subtract(filtered_image[:, :, 2], 50)

    elif filter_type == "decreased_blue":
        filtered_image[:, :, 0] = cv2.subtract(filtered_image[:, :, 0], 50)

    elif filter_type == "decreased_green":
        filtered_image[:, :, 1] = cv2.subtract(filtered_image[:, :, 1], 50)

        
    return filtered_image

image_path = "/Users/swagatmohanty/Documents/Python 2/pexels-pixelazteca-12002706.jpg"
image = cv2.imread(image_path)

if image is None:
    print("This image could not be found!")
else:
    filter_type = "orignal"

    print("Press the following keys to apply filters:")
    print("o --> Original Image")
    print("r --> Red Tint")
    print("b --> Blue Tint")
    print("g --> Green Tint")
    print("i --> Increased Red")
    print("w --> Increased Blue")
    print("e --> Increased Green")
    print("t --> Decreased Red")
    print("d --> Decreased Blue")
    print("y --> Decreased Green")
    print("q --> Quit")
    
    while True:
        filtered_image = apply_color_filter(image, filter_type)

        cv2.imshow("Filtered Image", filtered_image)

        key = cv2.waitKey(1) & 0xFF

        if key == ord('o'):
            filter_type = "orignal"
        elif key == ord('r'):
            filter_type = "red_tint"
        elif key == ord('b'):
            filter_type = "blue_tint"
        elif key == ord('g'):
            filter_type = "green_tint"
        elif key == ord('i'):
            filter_type = "increased_red"
        elif key == ord('w'):
                filter_type = "increased_blue"
        elif key == ord('e'):
                filter_type = "increased_green"
        elif key == ord('t'):
            filter_type = "decreased_red"
        elif key == ord('d'):
            filter_type = "decreased_blue"
        elif key == ord('y'):
            filter_type = "decreased_green"
        elif key == ord('q'):
           print("Exiting...")
           break
        else: 
            print("Invalid Key! Please use one of the above options")

cv2.destroyAllWindows()