from shape_recognition.src.shapes.shape import Shape
import cv2
import math
import numpy as np

epsilon = 0.04

class Circle(Shape):
    def __init__(self, contour: np.ndarray):
        super().__init__(contour)
        self.name = "Circle"
        self.radius = None
        self.area = 0

    def detect_shapes(self) -> bool:
        """
        Detect if the contour represents a circle by comparing the area
        of the contour with the area of the enclosing circle.

        Returns:
            bool: True if the shape is a circle, False otherwise.
        """
        # Approximate the contour to simplify its shape
        approx = cv2.approxPolyDP(self.contour, epsilon * cv2.arcLength(self.contour, True), True)
        # Check if the contour has exactly 6 vertices
        if len(approx) > 6:
            self.find_radius()
            # Compute the area of the contour
            contour_area = cv2.contourArea(self.contour)
            # Compute the area of the enclosing circle
            circle_area = math.pi * (self.radius ** 2)

            # Check if the contour area and circle area are similar
            # 15% tolerance
            return abs(contour_area - circle_area) / circle_area < 0.15
        return False
    def contour_shapes(self) -> float:
        """
        Calculate and return the area of the circle based on the radius.

        Returns:
            float: Area of the circle.
        """
        self.find_radius()
        self.area = round(math.pi * (self.radius ** 2), 2)
        return self.area

    def print_shape_info(self, img: cv2.Mat) -> None:
        """
        draw contours of the shape and information about shape
        Args:
            img (numpy.ndarray): The image on which to draw the shape.
        """
        self.find_center()
        self.find_radius()
        self.contour_shapes()

        texts = [f"{self.name}", f"radius: {self.radius}", f"area: {self.area}"]
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.drawContours(img, [self.contour], -1, (0, 255, 0), 2)
        x = self.c_x-20
        y = self.c_y
        for text in texts:
            cv2.putText(img, text, (x, y), font, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
            y = y+20

    def find_radius(self) -> None:
        """
        calculate the radius of the minimum enclosing circle for the contour
        """
        _, radius = cv2.minEnclosingCircle(self.contour)
        self.radius = round(radius, 2)
