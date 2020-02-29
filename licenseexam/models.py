from django.db import models
from django.contrib.auth.models import User
import datetime

class TestResult(models.Model):
    result_time = models.IntegerField()
    question_count = models.IntegerField()
    datetime_completed = models.TimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __init__(self, time, count):
        self.result_time = time
        self.question_count = count
        self.datetime_completed = datetime.datetime.now()
