from django.db import models
from django.contrib.auth.models import User


class TestResult(models.Model):
    result_time = models.IntegerField()
    question_count = models.IntegerField()
    datetime_completed = models.TimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
