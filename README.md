# OpenCV Django Demo

This project uses simple OpenCV integration for object detection (people in this specific case) and is combined with Django web application.

## Content
- `opencv_django_demo/` – Python module for image processing
- `opencv_site/` – Django project for showing image processing results

## Running
1. Install requirements:
```bash
pip install -r requirements.txt
```

2. Running Django server:
```bash
cd opencv_site
python manage.py runserver
```

3. Use `http://127.0.0.1:8000/` adress to test the image upload.

## 🧠 OpenCV funkcionalnost
OpenCV uses two approaches:
- HOG + SVM
- YOLOv8
