from django.contrib import messages
from django.shortcuts import render, redirect

from .models import PeopleCounting
from .image_proc_engine.image_processor_hog import detect_people_hog
from .image_proc_engine.image_processor_yolo import detect_people_yolo


# Create your views here.
def upload(request):
    if request.method == 'POST' and request.FILES.get('image'):
        uploaded_file = request.FILES['image']

        detection = PeopleCounting()
        detection.original_file.save(uploaded_file.name, uploaded_file)
        detection.save()

        image_path = detection.original_file.path
        yolo_path, yolo_count = detect_people_yolo(image_path)
        if yolo_path:
            detection.yolo_processed_file.name = yolo_path
            detection.yolo_people_counted = yolo_count

        hog_path, hog_count = detect_people_hog(image_path)
        if hog_path:
            detection.hog_processed_file.name = hog_path
            detection.hog_people_counted = hog_count

        detection.save()
        messages.success(request, "Image uploaded and analyzed successfully!")
        return redirect('dashboard:dashboard')
    return render(request, 'counter/counter-upload.html')