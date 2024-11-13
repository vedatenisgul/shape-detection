from abc import ABC, abstractmethod
# for abstract base class and abstract methods
import cv2
import numpy as np


class Shape(ABC):
    # abstract methods will be defined in subclasses
    def __init__(self, contour: np.ndarray):
        self.contour = contour
        self.c_x = 0
        self.c_y = 0

    @abstractmethod
    def detect_shapes(self) -> bool:
        pass

    @abstractmethod
    def contour_shapes(self) -> float:
        pass

    @abstractmethod
    def print_shape_info(self, img: cv2.Mat) -> None:
        pass

    def find_center(self) -> tuple:
        """Finds and returns the center coordinates (cx, cy) of the contour."""
        moments = cv2.moments(self.contour)
        if moments["m00"] != 0:
            self.c_x = int(moments["m10"] / moments["m00"])
            self.c_y = int(moments["m01"] / moments["m00"])
        else:
            self.c_x, self.c_y = 0, 0
        return self.c_x, self.c_y
