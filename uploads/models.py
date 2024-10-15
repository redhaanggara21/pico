from django.db import models
from PIL import Image
from .utils import get_filtered_image
import numpy as np
from io import BytesIO
from django.core.files.base import ContentFile

# Create your models here.
ACTION_CHOICES = (
    ('NO_FILTER', 'no filter'),
    ('COLORIZED', 'colorized'),
    ('GRAYSCALE', 'grayscale'),
    ('BLURRED', 'blurred'),
    ('BINARY', 'binary'),
    ('INVERT', 'invert')
)

class Upload(models.Model):
    image = models.ImageField(upload_to='images')
    action = models.CharField(max_length=250, choices=ACTION_CHOICES)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
    
    def save(self, *args, **kwargs):

        #open image
        pil_img = Image.open(self.image)

        #convert the image to array 
        cv_img = np.array(pil_img)
        img = get_filtered_image(cv_img, self.action)

        im_pill = Image.fromarray(img)

        buffer = BytesIO()
        im_pill.save(buffer, format='png')
        image_png = buffer.getvalue()

        self.image.save(str(self.image), ContentFile(image_png), save=False)

        super().save(args, **kwargs)

class Certificate(models.Model):
    user_name = models.CharField(max_length=255)
    certificate_image = models.ImageField(upload_to='certificates/')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name
