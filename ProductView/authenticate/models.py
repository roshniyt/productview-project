from django.db import models

# Create your models here.
class HeroSection(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='images/', default ="")

    def __str__(self):
        return self.description

class SampleResult(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', default="")

    def __str__(self):
        return self.title