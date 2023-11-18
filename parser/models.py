from django.db import models

# Create your models here.
class Mark(models.Model):
    mark_name = models.CharField(max_length=64)

    def __str__(self):
        return f'Марка :{self.mark_name}'


class Model(models.Model):
    model_name = models.CharField(max_length=64)
    modification = models.CharField(max_length=64, null=True)
    body_type = models.CharField(max_length=64, null=True)
    years = models.CharField(max_length=64, null=True)
    mark = models.ForeignKey(Mark, on_delete=models.CASCADE, related_name='all_models')
    
    
    def __str__(self):
        return f'Модель :{self.model_name} Модификация: {self.modification} Кузов: {self.body_type} года :{self.years}'