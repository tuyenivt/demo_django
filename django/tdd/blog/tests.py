from django.test import TestCase
from .models import Entry

class EntryModelTest(TestCase):

  def test_string_representation(self):
    entry = Entry(title='My entry title')
    self.assertEqual(str(entry), entry.title)
