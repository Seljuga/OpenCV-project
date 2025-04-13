from Image_processor_hog import detect_people
from Image_processor_yolo import detect_people_yolo

if __name__ == "__main__":
    image_path_1 = "test.jpg"
    image_path_2 = "test_2.jpg"
    result = detect_people(image_path_1)
    print(f"Image saved as: {result}")
    result = detect_people(image_path_2)
    print(f"Image saved as: {result}")

    result = detect_people_yolo(image_path_1)
    print(f"Image saved as: {result}")
    result = detect_people_yolo(image_path_2)
    print(f"Image saved as: {result}")
