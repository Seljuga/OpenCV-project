import sys
import os
from collections import defaultdict
from django.shortcuts import render

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'opencv_django_demo')))

from Image_processor_hog import detect_people as detect_people_hog
from Image_processor_yolo import detect_people_yolo


def normalize_filename(filename):
    name, _ = os.path.splitext(filename)
    return name.lower()


def upload_view(request):
    if request.method == "POST" and "clear" in request.POST:
        for folder in ["temp_results", "temp_uploads"]:
            for fname in os.listdir(folder):
                path = os.path.join(folder, fname)
                if os.path.isfile(path):
                    os.remove(path)

    image_results = defaultdict(lambda: {"original": "", "hog": "", "yolo": ""})

    if request.method == "POST" and "clear" not in request.POST:
        uploaded_files = request.FILES.getlist("image")
        os.makedirs("temp_uploads", exist_ok=True)

        for image_file in uploaded_files:
            original_name = os.path.basename(image_file.name)
            key = normalize_filename(original_name)

            upload_path = os.path.join("temp_uploads", original_name)

            try:
                with open(upload_path, "wb") as f:
                    for chunk in image_file.chunks():
                        f.write(chunk)
            except Exception as e:
                print(f"Error when saving the image: {e}")
                continue

            image_results[key]["original"] = upload_path.replace("\\", "/")

            hog_result = detect_people_hog(upload_path)
            yolo_result = detect_people_yolo(upload_path)

            image_results[key]["hog"] = hog_result.replace("\\", "/")
            image_results[key]["yolo"] = yolo_result.replace("\\", "/")

    uploads_dir = "temp_uploads"
    results_dir = "temp_results"

    if os.path.exists(uploads_dir):
        for fname in os.listdir(uploads_dir):
            key = normalize_filename(fname)
            full_path = os.path.join(uploads_dir, fname).replace("\\", "/")
            image_results[key]["original"] = full_path

    if os.path.exists(results_dir):
        for fname in os.listdir(results_dir):
            path = os.path.join(results_dir, fname).replace("\\", "/")
            lower_fname = fname.lower()

            if lower_fname.endswith("_hog.jpg"):
                key = lower_fname.replace("_hog.jpg", "")
                image_results[key]["hog"] = path
            elif lower_fname.endswith("_yolo.jpg"):
                key = lower_fname.replace("_yolo.jpg", "")
                image_results[key]["yolo"] = path

    return render(request, "upload.html", {"image_results": dict(image_results)})