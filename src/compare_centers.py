import math


# calculate the distance between center of the detected objects
def calculate_distance(center1: tuple, center2: tuple) -> float:
    """
    Calculate distance between two points (centers).
    """
    return math.sqrt((center1[0] - center2[0])**2 + (center1[1] - center2[1])**2)


# compare the centers of new shape to old shapes
def compare_centers(c_x: int, c_y: int, detected_centers: list, threshold: int) -> bool:
    """
    Compare the center (c_x, c_y) of a new shape to previously detected shape centers.

    Args:
        c_x (int): X coordinate of the new shape's center.
        c_y (int): Y coordinate of the new shape's center.
        detected_centers (list): List of previously detected center coordinates (x, y).
        threshold (int): The distance threshold to consider shapes as duplicates (default is 20).

    Returns:
        bool: True if the new shape's center is sufficiently far from existing ones, False if it's too close.
    """
    is_new_shape = True
    for (center_x, center_y) in detected_centers:
        if calculate_distance((c_x, c_y), (center_x, center_y)) < threshold:  # Mesafeyi ayarlayabilirsin
            is_new_shape = False
            break

    return is_new_shape
