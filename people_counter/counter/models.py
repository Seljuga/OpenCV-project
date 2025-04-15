import uuid

from django.db import models
from django.utils import timezone


# Create your models here.
def upload_to_original(instance, filename):
    return f'uploads/original/{uuid.uuid4()}.jpg'

def upload_to_yolo(instance, filename):
    return f'uploads/yolo/{uuid.uuid4()}.jpg'

def upload_to_hog(instance, filename):
    return f'uploads/hog/{uuid.uuid4()}.jpg'

class PeopleCounting(models.Model):
    original_file = models.ImageField(upload_to=upload_to_original)
    yolo_processed_file = models.ImageField(upload_to=upload_to_yolo, null=True, blank=True)
    hog_processed_file = models.ImageField(upload_to=upload_to_hog, null=True, blank=True)

    yolo_people_counted = models.IntegerField(null=True, blank=True)
    hog_people_counted = models.IntegerField(null=True, blank=True)

    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"People counting ({self.pk})"
