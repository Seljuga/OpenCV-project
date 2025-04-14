import os
import uuid
import cv2

def detect_people(image_path, output_path):
    image = cv2.imread(image_path)

    if image is None:
        print(f"Image not found: {image_path}")
        return None

    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    # Current implementation using default HOG (Histogram of Oriented Gradients) + SVM model from OpenCV-a
    (regions, _) = hog.detectMultiScale(image, winStride=(4, 4), padding=(8, 8), scale=1.05)

    num_people_detected = len(regions)

    for (x, y, w, h) in regions:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    os.makedirs(output_path, exist_ok=True)
    filename = os.path.basename(image_path)
    result_filename = os.path.join(output_path, f"output_{filename}_hog.jpg")
    saved = cv2.imwrite(result_filename, image)

    if saved:
        print(f"Result saved as: {result_filename}")
        try:
            os.startfile(result_filename)
        except Exception as e:
            print(f"Can't open the image using automated process: {e}")
        return result_filename, num_people_detected
    else:
        print("Couldn't save image.")
        return None, num_people_detected