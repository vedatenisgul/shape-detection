from shape_recognition.src.shapes.shape import Shape
import cv2
import numpy as np
import math

epsilon = 0.02

class Ellipse(Shape):
    def __init__(self, contour: np.ndarray):
        super().__init__(contour)
        self.name = "Ellipse"
        self.area = 0

    def detect_shapes(self) -> bool:
        """
        Detect if the contour represents an ellipse by comparing the area
        of the contour with the area of the fitted ellipse.

        Returns:
            bool: True if the shape is an ellipse, False otherwise.
        """
        # Approximate the contour to simplify its shape
        approx = cv2.approxPolyDP(self.contour, epsilon * cv2.arcLength(self.contour, True), True)
        # Check if the contour has more than 6 vertices
        if len(approx) > 6:
            # compare actual area of contour to the area of fitted ellipse if error rate below %10 return true
            return abs(self.contour_shapes() - cv2.contourArea(self.contour))/cv2.contourArea(self.contour) < 0.1

        return False

    def contour_shapes(self) -> float:
        """
        Fits an ellipse to the contour and calculates the area of the ellipse.

        Returns:
            float: Area of the fitted ellipse.
        """
        # Fit an ellipse to the contour
        ellipse = cv2.fitEllipse(self.contour)

        # Get the axes lengths (semi-major and semi-minor axes)
        (center, axes, angle) = ellipse
        a = axes[0] / 2  # semi-major axis
        b = axes[1] / 2  # semi-minor axis

        # Calculate the area of the ellipse
        self.area = round(math.pi * a * b, 2)
        return self.area

    def print_shape_info(self, img: cv2.Mat) -> None:
        """
        draw contours of the shape and information about shape
        Args:
            img (numpy.ndarray): The image on which to draw the shape.
        """
        self.find_center()
        self.contour_shapes()

        texts = [f"{self.name}", f"area:{self.area}"]
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.drawContours(img, [self.contour], -1, (0, 255, 0), 2)
        x = self.c_x-20
        y = self.c_y
        for text in texts:
            cv2.putText(img, text, (x, y), font, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
            y = y+20
