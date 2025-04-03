# Shape Recognition

**Shape Recognition** is a Python project designed for detecting geometric shapes in images using OpenCV. The project includes different shape recognition algorithms and allows users to detect various shapes like rectangles, squares, circles, triangles, ellipses, hexagons, and pentagons. Detected shapes are processed to prevent duplicate detections by comparing their center positions.

## Features

- **Shape Detection**: Detects geometric shapes such as squares, rectangles, circles, triangles, hexagons, pentagons, and ellipses.
- **Center Comparison**: Prevents false detections of already identified shapes by comparing the centers of detected objects.
- **Contour and Area Calculation**: Draws contours on the image and calculates the area of the detected shapes.
- **Image Processing**: Uses grayscale conversion, Gaussian blur, and edge detection (Canny) for better shape identification.
- **Shape Types**: 
    - Square
    - Rectangle
    - Circle
    - Triangle
    - Pentagon
    - Hexagon
    - Ellipse

## Prerequisites

Make sure to have the following installed:

- Python 3.x
- OpenCV (`cv2`)
- NumPy (`numpy`)
- `math`
- `os`
- `ABC` and `abstractmethod` from the `abc` module (for abstract base classes)

To install the necessary dependencies, you can run:

```bash
pip install opencv-python numpy
```

## Project Structure
```bash
shape_recognition/
│
├── src/
│   ├── shapes/
│   │   ├── __init__.py         
│   │   ├── shapes.py            
│   │   ├── square.py
│   │   ├── circle.py
│   │   ├── ellipse.py
│   │   ├── triangle.py
│   │   ├── hexagon.py
│   │   ├── rectangle.py
│   │   └── pentagon.py
│   ├── __init__.py              
│   ├── shape_detection.py
│   ├── compare_centers.py
│   ├── shape_recognition.py
│   └── main.py                  
│
├── assets/
│   └── img2.png
│
├── README.md
├── report.md
├── output.png
├── LICENSE
└── .gitignore

```
## Important Files

- **shape_detection.py**: Contains the main logic for detecting shapes in an image.
- **compare_centers.py**: Handles the logic for comparing the centers of detected shapes to avoid multiple detections of the same shape.
- **shapes/*.py**: Contains individual shape classes (e.g., Rectangle, Square, Circle, etc.) with methods to detect and analyze the shapes.
- **main.py**: Entry point of the program. It loads an image, applies shape detection, and displays the result.
