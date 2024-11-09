from shape_recognition.src.shapes.shape import Shape
import cv2
import math
import numpy as np

epsilon = 0.03

class Pentagon(Shape):
    def __init__(self, contour: np.ndarray):
        super().__init__(contour)
        self.name = "Pentagon"
        self.area = 0

    def detect_shapes(self) -> bool:
        """
        Detect if the contour represents a pentagon by checking if the contour
        has exactly 5 vertices.

        Returns:
            bool: True if the shape is a pentagon, False otherwise.
        """
        # Approximate the contour with a polygon
        approx = cv2.approxPolyDP(self.contour, epsilon * cv2.arcLength(self.contour, True), True)
        if len(approx) == 5:
            return True
        return False

    def contour_shapes(self) -> float:
        """
        Calculate the area of the pentagon based on its side length.

        Returns:
            float: The area of the pentagon.
        """
        approx = cv2.approxPolyDP(self.contour, 0.03 * cv2.arcLength(self.contour, True), True)
        if len(approx) == 5:
            side_length = cv2.norm(approx[0][0] - approx[1][0])  # Distance between first and second vertex

            # For a regular pentagon, we can use the formula to calculate the area from side length
            self.area = round((1 / 4) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * (side_length ** 2), 2)
        return self.area

    def print_shape_info(self, img: cv2.Mat) -> None:
        """
        Draw the pentagon contour on the image and display its name and area.

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
