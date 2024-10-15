from django.db import models

# Create your models here.
class Certificate(models.Model):
    user_name = models.CharField(max_length=255)
    certificate_image = models.ImageField(upload_to='certificates/')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name