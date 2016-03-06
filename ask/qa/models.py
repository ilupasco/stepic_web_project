from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
  title = models.CharField(max_length=255)
  text = models.TextField()
  added_at = models.DateTimeField(null=False, auto_now_add=True)
  rating = models.IntegerField(null=False, default=0)
  author = models.ForeignKey(User, related_name='user_author')
  likes = models.ManyToManyField(User, related_name='user_likes')

  def __unicode__(self):
    return self.title

  def get_absolute_url(self):
    return '/question/%d/' % self.pk

  class Meta:
    db_table = 'question'
    ordering = ['-creation_date']


class Answer(models.Model):
  text = models.TextField()
  added_at = models.DateTimeField(null=False, auto_now_add=True)
  question = models.ForeignKey(Question)
  author = models.ForeignKey(User)

  def __unicode__(self):
    return self.title
