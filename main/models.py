from django.db import models

class Traveler(models.Model):
    name = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    count = models.IntegerField(default=0)
    data = models.JSONField()
    
    def __str__(self):
        return self.name
    
    def show_survey(self):
        results = ['accuracy', 'satisfaction', 'influence']
        survey = self.data["survey"]
        count = 0
        print(f'{self.name}')
        for result in results:
            count = survey[result].count(1) + survey[result].count(2)
            if count > len(survey[result])/2:
                print(f'- {result}: 목표 미달성')
            else:
                print(f'- {result}: 목표 충족')
        print('----------------------')
    
class Question(models.Model):
    num = models.IntegerField(unique=True)
    data = models.JSONField()
    
    def __str__(self):
        return self.num
    
class Choice(models.Model):
    content = models.CharField(max_length=100)
    question_id = models.ForeignKey(to='main.Question', on_delete=models.CASCADE)
    category = models.CharField(max_length=1)
    
    def __str__(self):
        return self.content

