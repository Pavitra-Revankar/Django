from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse


class Question(models.Model):
    question = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='like')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.question



    def get_absolute_url(self):
        return reverse('question', args=(str(self.id)))


class Answer(models.Model):
    Questions = models.ForeignKey(Question, related_name="answer", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.Questions.question


