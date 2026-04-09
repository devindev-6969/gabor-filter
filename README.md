# Gabor Filter Texture Explorer

A small computer vision project I built while experimenting with image processing and texture analysis.

This project uses **Gabor filters** to analyze grayscale images and highlight textures and edges in different directions.
I wanted to explore how directional filters respond to patterns such as fabric textures, natural surfaces, and structural edges.

## What it does

* Loads grayscale images
* Applies Gabor filters at multiple orientations
* Highlights directional edges and textures
* Visualizes how image features change with angle

## Orientations used

The filter is applied at:

* 0°
* 45°
* 90°
* 135°

This helps in observing horizontal, vertical, and diagonal edge responses.

## Tech Stack

* Python
* OpenCV
* NumPy
* Matplotlib

## Why I made this

I was exploring classical image processing techniques and wanted to better understand how orientation-sensitive filters work in texture detection and edge analysis.

It was a fun little experiment to visualize how the same image responds differently depending on filter direction.

## Sample Use Cases

This kind of filtering is useful in:

* texture recognition
* fingerprint analysis
* edge detection
* feature extraction
* computer vision preprocessing

## Run locally

```bash
pip install opencv-python numpy matplotlib
python gabor_filter_5images.py
```

## Future ideas

* try multiple scales / wavelengths
* compare with Sobel and Canny filters
* use it for fingerprint matching
* integrate into a small CV demo app
