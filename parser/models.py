from django.db import models


class Mark(models.Model):
    mark_name = models.CharField(max_length=64)

    def __str__(self):
        return f'Марка :{self.mark_name}'


class Model(models.Model):
    model_name = models.CharField(max_length=64)
    mark = models.ForeignKey(Mark, on_delete=models.CASCADE, related_name='all_models')
    
    
    def __str__(self):
        return f'Модель :{self.model_name}' 