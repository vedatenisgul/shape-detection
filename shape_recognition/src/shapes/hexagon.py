from shape_recognition.src.shapes.shape import Shape
import cv2
import math
import numpy as np

epsilon = 0.04

class Hexagon(Shape):
    def __init__(self, contour: np.ndarray):
        super().__init__(contour)
        self.name = "Hexagon"
        self.area = 0
        self.side_length = 0

    def detect_shapes(self) -> bool:
        """
        Detect if the contour represents a hexagon by checking if the shape
        has 6 vertices and comparing the area of the contour with the area
        of the fitted regular hexagon.

        Returns:
            bool: True if the shape is a hexagon, False otherwise.
        """
        # Approximate the contour to simplify its shape
        approx = cv2.approxPolyDP(self.contour, epsilon * cv2.arcLength(self.contour, True), True)
        # Check if the contour has exactly 6 vertices
        if len(approx) == 6:
            return abs(self.contour_shapes() - cv2.contourArea(self.contour))/cv2.contourArea(self.contour) < 0.1

        return False

    def contour_shapes(self) -> float:
        """
        Calculate the area of the regular hexagon based on the side length.

        Returns:
            float: Area of the hexagon.
        """
        if self.find_side_length():
            # For a regular hexagon, use the formula to calculate the area from side length
            self.area = round((3 * math.sqrt(3) / 2) * (self.side_length ** 2), 2)

        return self.area

    def print_shape_info(self, img: cv2.Mat) -> None:
        """
        Draw the contour of the hexagon on the image and display its name.

        Args:
            img (cv2.Mat): The image on which the shape will be drawn.
        """
        self.find_center()
        self.find_side_length()
        self.contour_shapes()

        texts = [f"{self.name}", f"area:{self.area}"]
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.drawContours(img, [self.contour], -1, (0, 255, 0), 2)
        x = self.c_x - 20
        y = self.c_y
        for text in texts:
            cv2.putText(img, text, (x, y), font, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
            y = y + 20

    def find_side_length(self) -> float:
        """
        Calculate the side length of the hexagon by measuring the distance
        between two consecutive vertices of the approximated contour.

        Returns:
            float: The side length of the hexagon.
        """
        approx = cv2.approxPolyDP(self.contour, 0.03 * cv2.arcLength(self.contour, True), True)
        # If the shape has 6 vertices, calculate the side length
        if len(approx) == 6:
            self.side_length = cv2.norm(approx[0][0] - approx[1][0])  # Distance between first and second vertex
        return self.side_length
