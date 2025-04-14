from Image_processor_hog import detect_people
from Image_processor_yolo import detect_people_yolo

if __name__ == "__main__":
    output_path = "D:\Algebra\OpenCV\OutputFolder"
    image_path_1 = "test.jpg"
    image_path_2 = "test_2.jpg"
    result, num_people_detected = detect_people(image_path_1, output_path)
    print(f"Image saved as: {result}")
    print(f"Number of detections in image: {num_people_detected}")
    result, num_people_detected = detect_people(image_path_2, output_path)
    print(f"Image saved as: {result}")
    print(f"Number of detections in image: {num_people_detected}")

    result, num_people_detected = detect_people_yolo(image_path_1, output_path)
    print(f"Image saved as: {result}")
    print(f"Number of detections in image: {num_people_detected}")
    result, num_people_detected = detect_people_yolo(image_path_2, output_path)
    print(f"Image saved as: {result}")
    print(f"Number of detections in image: {num_people_detected}")
