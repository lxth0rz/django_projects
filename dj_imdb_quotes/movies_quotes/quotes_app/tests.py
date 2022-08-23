import datetime
from .models import Keyword
from django.test import TestCase
from django.utils import timezone


class KeywordModelTests(TestCase):

    def test_was_added_recently_with_future_question(self):
        """
        was_added_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Keyword(pub_date=time)
        self.assertIs(future_question.was_added_recently(), False)
