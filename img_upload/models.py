from django.db import models

class Upload(models.Model):
    image=models.ImageField(upload_to="images/")
    img_name=models.TextField()
    ocr=models.TextField()
    def __str__(self):
        return self.img_name