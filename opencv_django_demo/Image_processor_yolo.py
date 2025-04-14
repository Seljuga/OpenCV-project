import uuid
import os
from ultralytics import YOLO
import cv2

#Use nano version of yolo
model = YOLO("yolov8n.pt")

def detect_people_yolo(image_path, output_path):
    image = cv2.imread(image_path)
    if image is None:
        print(f"Image not found: {image_path}")
        return None

    results = model(image)
    people = [box for box in results[0].boxes.data if int(box[-1]) == 0]
    num_people_detected = len(people)

    for box in people:
        x1, y1, x2, y2, score, cls = box
        cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)


    os.makedirs(output_path, exist_ok=True)
    filename = os.path.basename(image_path)
    result_filename = os.path.join(output_path, f"output_{filename}_yolo.jpg")
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