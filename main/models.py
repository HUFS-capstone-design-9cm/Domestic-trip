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

    def show_result(self):
        travelers = Traveler.objects.all()
        accuracy = 0
        satisfaction = 0
        influence = 0
        count = 0
        for traveler in travelers:
            count += traveler.count
            survey = traveler.data["survey"]
            accuracy += survey['accuracy'].count(1) + survey['accuracy'].count(2)
            satisfaction += survey['satisfaction'].count(1) + survey['satisfaction'].count(2)
            influence += survey['influence'].count(1) + survey['influence'].count(2)

        print(accuracy, accuracy/count)
        print(satisfaction, satisfaction/count)
        print(influence, influence/count)

    def total_mean(self):
        travelers = Traveler.objects.all()
        accuracy = 0
        satisfaction = 0
        influence = 0
        count = 0
        for traveler in travelers:
            count += traveler.count
            survey = traveler.data["survey"]
            accuracy += sum(survey['accuracy'])
            satisfaction += sum(survey['satisfaction'])
            influence += sum(survey['influence'])
        print(accuracy/count)
        print(satisfaction/count)
        print(influence/count)

    def get_mean(self):
        travelers = Traveler.objects.all()
        for traveler in travelers:
            count = traveler.count
            survey = traveler.data["survey"]
            accuracy = sum(survey['accuracy'])
            satisfaction = sum(survey['satisfaction'])
            influence = sum(survey['influence'])
            print(traveler.name)
            print(accuracy/count)
            print(satisfaction/count)
            print(influence/count)
            print('=========================')


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

