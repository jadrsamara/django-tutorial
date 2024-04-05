"""
Models module fot the app: Polls

has:
- Question
- Choice
"""
from datetime import timedelta
from django.db import models
from django.utils import timezone

class Question(models.Model):
    """
    Question model
    """
    question_text = models.CharField(max_length=256)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return str(self.question_text)

    def was_published_recently(self):
        """
        checks if the question was published in the last day
        """
        return self.pub_date >= timezone.now() - timedelta(days=1)


class Choice(models.Model):
    """
    Choice model
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=256)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.choice_text)
