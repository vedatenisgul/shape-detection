from shape_recognition.src.shapes.shape import Shape
import cv2
import math
import numpy as np


class Triangle(Shape):
    def __init__(self, contour: np.ndarray):
        super().__init__(contour)
        self.name = "Triangle"
        self.c_x = None
        self.c_y = None
        self.area = 0

    def detect_shapes(self) -> bool:
        """
        Detect if the contour represents a triangle by approximating the contour
        and checking if it has 3 vertices.

        Returns:
            bool: True if the shape is a triangle, False otherwise.
        """
        # check if there is 3 edges
        approx = cv2.approxPolyDP(self.contour, 0.04 * cv2.arcLength(self.contour, True), True)
        if len(approx) == 3:
            return True
        return False

    def contour_shapes(self) -> float:
        """
        Calculate the area of the triangle using Heron's formula.

        Returns:
            float: The area of the triangle.
        """
        # Approximate the contour to a polygon (triangle should have 3 vertices)
        approx = cv2.approxPolyDP(self.contour, 0.03 * cv2.arcLength(self.contour, True), True)

        # Check if it's a triangle (3 vertices)
        if len(approx) == 3:
            # Calculate the lengths of the sides of the triangle
            side1 = cv2.norm(approx[0][0] - approx[1][0])  # Distance between vertex 1 and 2
            side2 = cv2.norm(approx[1][0] - approx[2][0])  # Distance between vertex 2 and 3
            side3 = cv2.norm(approx[2][0] - approx[0][0])  # Distance between vertex 3 and 1

            # Use Heron's formula to calculate the area of the triangle
            s = (side1 + side2 + side3) / 2  # Semi-perimeter
            area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))  # Heron's formula
            self.area = round(area, 2)
        return self.area

    def print_shape_info(self, img: cv2.Mat) -> None:
        """
        Draw the square contour on the image and display its name and area.

        Args:
            img (cv2.Mat): The image on which the shape will be drawn.
        """
        self.find_center()
        self.contour_shapes()

        texts = [f"{self.name}", f"area:{self.area}"]
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.drawContours(img, [self.contour], -1, (0, 255, 0), 2)
        x = self.c_x - 20
        y = self.c_y
        for text in texts:
            cv2.putText(img, text, (x, y), font, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
            y = y + 20
