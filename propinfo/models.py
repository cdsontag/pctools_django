from django.db import models

# Create your models here. (pctools note:  we don't have to bake Models sinto the design)

class Program(models.Model):
    program_id = models.IntegerField(default=0) # can't use id, clashes with django
    def __str__(self): return self.program_id

class Investigator(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    def __str__(self): return f'{last_name}, {first_name}'
