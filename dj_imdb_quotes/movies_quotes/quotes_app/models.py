import datetime

from django.db import models
from django.utils import timezone


class Keyword(models.Model):
    keyword_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.keyword_text

    def was_added_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Quote(models.Model):
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)
    quote_text = models.CharField(max_length=2000)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.quote_text
