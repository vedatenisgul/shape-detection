from shape_recognition.src.shapes.shape import Shape
import cv2
import numpy as np


class Square(Shape):
    def __init__(self, contour: np.ndarray):
        super().__init__(contour)
        self.name = "Square"
        self.width = None
        self.height = None
        self.area = 0

    def detect_shapes(self) -> bool:
        """
        Detect if the contour represents a square by approximating the contour
        and checking if it has 4 sides and an aspect ratio close to 1.

        Returns:
            bool: True if the shape is a square, False otherwise.
        """
        approx = cv2.approxPolyDP(self.contour, 0.04 * cv2.arcLength(self.contour, True), True)
        if len(approx) == 4:  # Square has 4 sides
            x, y, w, h = cv2.boundingRect(approx)
            aspect_ratio = float(w) / h
            if abs(aspect_ratio - 1) <= 0.2:  # Square has equal width and height
                return True
        return False

    def contour_shapes(self) -> float:
        """
        Calculate the area of the square based on its bounding rectangle.

        Returns:
            float: The area of the square.
        """
        # Calculate the bounding rectangle for the given contour (approx).
        # The function returns the top-left corner coordinates (x, y) and the width (w) and height (h)
        # of the smallest rectangle that can enclose the contour.
        approx = cv2.approxPolyDP(self.contour, 0.04 * cv2.arcLength(self.contour, True), True)
        if len(approx) == 4:
            x, y, w, h = cv2.boundingRect(approx)
            self.width = w
            self.height = h
            self.area = round(w*h, 2)

        return self.area

    def print_shape_info(self, img: cv2.Mat) -> None:
        """
        Draw the square contour on the image and display its name and area.

        Args:
            img (cv2.Mat): The image on which the shape will be drawn.
        """
        self.find_center()
        self.contour_shapes()

        self.contour_shapes()

        texts = [f"{self.name}", f"area:{self.area}"]
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.drawContours(img, [self.contour], -1, (0, 255, 0), 2)
        x = self.c_x - 20
        y = self.c_y
        for text in texts:
            cv2.putText(img, text, (x, y), font, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
            y = y + 20

