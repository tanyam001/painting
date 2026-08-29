from django.db import models

class Painting(models.Model):
    painting_name = models.CharField(max_length=100)
    year_drawn = models.CharField(null=True, blank=True, max_length=6)
    image = models.ImageField(upload_to="paintings/")
    width = models.DecimalField(null=True, blank=True, max_digits=4, decimal_places=1)
    height = models.DecimalField(null=True, blank=True, max_digits=4, decimal_places=1)
    summary = models.CharField(null=True, blank=True, max_length=255)
    price = models.IntegerField(
        null = True, 
        blank = True
    )

    def __str__(self):
        return self.painting_name

    def dimensions(self):
        return f"{self.width} x {self.height} cm"

    #in template {{ painting.dimensions }}