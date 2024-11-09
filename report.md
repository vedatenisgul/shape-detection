# Shape Detection Program

## Introduction

In this project, a shape detection program has been developed using the OpenCV library. The program is designed to detect various geometric shapes (rectangle, circle, triangle, etc.) in an image and display information about each detected shape. Shape detection is done using edge detection and contour analysis. Additionally, a class-based structure is used to represent each detected shape.

## Methods Used

### 1. Shape Detection (Contour Detection)

The shape detection process consists of the following steps:

- **Grayscale Conversion**: The image is converted to grayscale, which simplifies the processing by eliminating unnecessary color information.
  
- **Gaussian Blur**: Gaussian blur is applied to the image to reduce noise. This helps in decreasing false positives during edge detection.

- **Edge Detection**: Canny edge detection is applied to the image to identify the edges, which are then used to extract the contours of the shapes.

- **Contour Detection**: After edge detection, the `cv2.findContours()` function is used to detect contours from the edges. This function finds the boundaries of the shapes in the image.

### 2. Shape Classification

Shape classification is performed by analyzing the contours. For each shape, a separate class is defined. These classes determine the type of shape (e.g., rectangle, triangle, circle) and its geometric properties (area, number of sides, etc.).

For example, when detecting a rectangle, if a contour has 4 sides, it is considered a rectangle. Additionally, `cv2.boundingRect()` is used to calculate the area of the rectangle.

### 3. Finding the Center of the Shape

The center of each detected shape is calculated using the `cv2.moments()` function. This function calculates the centroid (center of mass) of the contour, which represents the center of the shape. The center information is then used to label the shape and display it on the image.

### 4. Avoiding Duplicate Detections

When a new shape is detected, its center is compared with the centers of previously detected shapes. If the center of the new shape is too close to any previously detected shape (for example, within 20 pixels), it is considered a duplicate and not added to the list. This helps in avoiding multiple detections of the same shape.

### 5. Displaying Shape Information on the Image

For each detected shape, its contour is drawn on the image, and the shape's name (e.g., "Rectangle") and area are displayed next to the shape. This provides the user with quick information about the detected shape directly on the image.

## Challenges Faced

### 1. Parameter Adjustments

The parameters used for shape detection, especially the epsilon value and Gaussian blur settings, vary depending on the image being processed. For instance, in images with different sizes of shapes, the `cv2.approxPolyDP()` function’s epsilon parameter needs to be adjusted. The epsilon value controls the approximation of the contour. If it’s too small, too many details are captured; if it’s too large, the shapes may not be detected accurately.

Additionally, the thresholds for Canny edge detection (the lower and upper limits) must be adjusted to match the characteristics of the image. These threshold values directly impact the accuracy of edge detection.

### 2. Shape Variety and Complexity

Different shapes and sometimes irregular shapes with non-straight edges make detection challenging. For example, shapes with rounded edges, like circles or ellipses, can be difficult to detect properly. Accurate detection of these shapes requires careful fine-tuning of edge detection and contour detection steps.

### 3. Image Quality and Noise

Some images may contain low resolution or high noise levels, which can make the edges unclear. This can complicate the edge detection and contour detection process.

## Results

The program is capable of correctly detecting basic geometric shapes in a given image. It also computes the area and center of each shape and displays this information on the image. The shapes are drawn on the image, and their names and areas are labeled next to them, providing clear information to the user.

It’s important to note that the parameters (such as Gaussian blur and epsilon value) must be adjusted according to the specific image. Manual adjustments are needed for each different image to achieve the best results.

