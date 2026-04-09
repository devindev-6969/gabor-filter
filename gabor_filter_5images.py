import cv2
import numpy as np
import matplotlib.pyplot as plt

# List of image names
image_files = ['img1.jpg', 'img2.jpg', 'img3.jpg', 'img4.jpg', 'img5.jpg']

# Gabor parameters
ksize = 31
sigma = 4.0
lambd = 10.0
gamma = 0.5
psi = 0

# Orientations
orientations = [0, np.pi/4, np.pi/2, 3*np.pi/4]
titles = ['0°', '45°', '90°', '135°']

for image_file in image_files:
    img = cv2.imread(image_file, cv2.IMREAD_GRAYSCALE)

    if img is None:
        print(f"Could not load {image_file}")
        continue

    plt.figure(figsize=(12, 8))

    # Original image
    plt.subplot(2, 3, 1)
    plt.imshow(img, cmap='gray')
    plt.title("Original")
    plt.axis('off')

    # Apply filter at each orientation
    for i, theta in enumerate(orientations):
        kernel = cv2.getGaborKernel(
            (ksize, ksize),
            sigma,
            theta,
            lambd,
            gamma,
            psi,
            ktype=cv2.CV_32F
        )

        filtered_img = cv2.filter2D(img, cv2.CV_8UC3, kernel)

        plt.subplot(2, 3, i + 2)
        plt.imshow(filtered_img, cmap='gray')
        plt.title(f"{titles[i]}")
        plt.axis('off')

    plt.suptitle(f"Results for {image_file}")
    plt.tight_layout()
    plt.show()