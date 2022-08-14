from django.db import models


class Keyword(models.Model):
    keyword_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Quote(models.Model):
    question = models.ForeignKey(Keyword, on_delete=models.CASCADE)
    quote_text = models.CharField(max_length=2000)
    votes = models.IntegerField(default=0)
