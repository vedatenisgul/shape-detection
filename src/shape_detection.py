import cv2
from shape_recognition.src.shapes.square import Square
from shape_recognition.src.shapes.circle import Circle
from shape_recognition.src.shapes.ellipse import Ellipse
from shape_recognition.src.shapes.triangle import Triangle
from shape_recognition.src.shapes.hexagon import Hexagon
from shape_recognition.src.shapes.rectangle import Rectangle
from shape_recognition.src.shapes.pentagon import Pentagon
from shape_recognition.src.compare_centers import compare_centers

# store detected shapes center in a list to prevent second detection of same shape
detected_centers = []


def detect_shapes(img: cv2.Mat) -> list:
    # RGB values are multiplied by some values and converted to only one value for each pixel(grayscale)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Gaussian Blur to smooth the image.
    # Each pixel's value is adjusted based on the weighted average of its neighbors
    # using a Gaussian kernel, which reduces noise and detail.
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    # Edge Detection
    # Pixels with gradient values above 80 are considered edges,
    # while those below 30 are discarded. Values between 30 and 80 are
    # checked for continuity to determine if they should be considered edges.
    edges = cv2.Canny(blurred, 30, 80)

    # show the result of these steps
    gray_resized = cv2.resize(gray, (img.shape[1], img.shape[0]))
    blurred_resized = cv2.resize(blurred, (img.shape[1], img.shape[0]))
    edges_resized = cv2.resize(edges, (img.shape[1], img.shape[0]))
    combined_image = cv2.hconcat([gray_resized, blurred_resized, edges_resized])
    cv2.imshow("Combined Output", combined_image)
    # Find contours in the edge-detected image.
    # RETR_TREE retrieves all contours and organizes them into a hierarchical tree structure.
    # CHAIN_APPROX_SIMPLE compresses horizontal, vertical, and diagonal segments to save memory.
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # list for storing names of shapes
    shapes = []
    for contour in contours:
        # check for contours with area over 1000 to prevent unnecessary detections
        if cv2.contourArea(contour) > 1000:
            # list with various kind of shapes objects
            shape_list = [Triangle(contour), Square(contour), Rectangle(contour), Pentagon(contour), Hexagon(contour),
                          Circle(contour), Ellipse(contour)]

            for shape in shape_list:
                # check whether we can identify shape or not
                detected_shape = shape.detect_shapes()
                if detected_shape:
                    c_x, c_y = shape.find_center()
                    if compare_centers(c_x, c_y, detected_centers, 20):
                        detected_centers.append((c_x, c_y))
                        shape.print_shape_info(img)
                        print(f"Detected shape: {type(shape).__name__}, {shape.contour_shapes()}")
                        shapes.append(shape)
                    break

    return shapes
