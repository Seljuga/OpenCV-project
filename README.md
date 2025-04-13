
# OpenCV Django Demo

Ovaj projekt prikazuje jednostavnu integraciju OpenCV obrade slike (detekcija ljudi) s Django web aplikacijom.

## 📦 Sadržaj
- `opencv_django_demo/` – Python modul za obradu slike
- `opencv_site/` – Django projekt s upload formom i prikazom rezultata

## 🚀 Pokretanje
1. Instaliraj ovisnosti:
```bash
pip install -r requirements.txt
```

2. Pokreni Django server:
```bash
cd opencv_site
python manage.py runserver
```

3. Posjeti `http://127.0.0.1:8000/` i testiraj upload slike.

## 🧠 OpenCV funkcionalnost
Koristi HOG + SVM za detekciju ljudi na slici i vraća sliku s označenim osobama.

## 📂 Media folder
Rezultati se spremaju u `media/processed/`. Django automatski servira taj sadržaj preko `MEDIA_URL`.

Uživaj u demonstraciji!
