from django.db import models

class Traveler(models.Model):
    name = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    content = models.CharField(max_length=100)
    count = models.IntegerField(default=0)
    personality = models.CharField(max_length=3)
    
    def __str__(self):
        return self.name
    
class Question(models.Model):
    num = models.IntegerField(unique=True)
    content = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.num}. {self.content}'
    
class Choice(models.Model):
    content = models.CharField(max_length=100)
    question_id = models.ForeignKey(to='main.Question', on_delete=models.CASCADE)
    category = models.CharField(max_length=1)
    
    def __str__(self):
        return self.content
    
class Spot(models.Model):
    name = models.CharField(max_length=50)
    spot_id = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    traveler_id = models.ForeignKey(to='main.Traveler', on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f'{self.name} - {self.content}'
    
class Survey(models.Model):
    accuracy = models.IntegerField(default=0)
    satisfaction = models.IntegerField(default=0)
    influence = models.IntegerField(default=0)
    
    def __str__(self):
        return f'{self.accuracy}\n{self.satisfaction}\n{self.influence}'
    
