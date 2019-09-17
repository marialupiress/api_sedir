from django.db import models

# Create your models here.
class todoitem(models.Model) :
    text = models.TextField()
    dtime = models.DateField(auto_now_add=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.text
