from django.db import models
from imagekit.models import ImageSpecField  #썸네일
from imagekit.processors import ResizeToFill    #썸네일

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    image = models.ImageField(null=True, default='', upload_to="blogimg")
    image_thumbnail = ImageSpecField(source = 'image',processors=[ResizeToFill(250,250)])
    body = models.TextField()

    def __str__(self):
        return self.title