from shape_recognition.src.shape_detection import detect_shapes
import cv2
import os


def main():
    base_dir = os.path.dirname(__file__)
    img_path = os.path.join(base_dir, "../assets/img2.png")
    # convert image info to numpy array in format [0, 0, 255], ... for each pixel
    img = cv2.imread(img_path)
    if img is None:
        print("Error: Image not found!")
        return

    # Detect shapes in image
    shapes = detect_shapes(img)
    print(shapes)
    # Show result
    cv2.imshow("Detected Shapes", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
