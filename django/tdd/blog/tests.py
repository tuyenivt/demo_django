from django.test import TestCase
from django.contrib.auth import get_user_model
from .forms import CommentForm
from .models import Entry, Comment

class EntryModelTest(TestCase):

  def test_string_representation(self):
    entry = Entry(title='My entry title')
    self.assertEqual(str(entry), entry.title)

  def test_verbose_name_plural(self):
    self.assertEqual(str(Entry._meta.verbose_name_plural), "entries")

  def test_get_absolute_url(self):
    user = get_user_model().objects.create(username='some_user')
    entry = Entry.objects.create(title='title', body='body', author=user)
    self.assertIsNotNone(entry.get_absolute_url())

class ProjectTest(TestCase):

  def test_homepage(self):
    response = self.client.get('/')
    self.assertEqual(response.status_code, 200)

class HomePageTests(TestCase):

  """ Test whether our blog entries show up on the homepage """

  def setUp(self):
    self.user = get_user_model().objects.create(username='some_user')

  def test_no_entry(self):
    response = self.client.get('/')
    self.assertContains(response, 'No blog entries yet.')

  def test_one_entry(self):
    Entry.objects.create(title='1-title', body='1-body', author=self.user)
    response = self.client.get('/')
    self.assertContains(response, '1-title')
    self.assertContains(response, '1-body')

  def test_two_entry(self):
    Entry.objects.create(title='1-title', body='1-body', author=self.user)
    Entry.objects.create(title='2-title', body='2-body', author=self.user)
    response = self.client.get('/')
    self.assertContains(response, '1-title')
    self.assertContains(response, '1-body')
    self.assertContains(response, '2-title')

class EntryViewTest(TestCase):

  def setUp(self):
    self.user = get_user_model().objects.create(username='some_user')
    self.entry = Entry.objects.create(title='title-1', body='body-1', author=self.user)
    self.comment = Comment.objects.create(entry=self.entry, name='name-1', email='email-1@coloza.com', body='body-1')

  def test_basic_view(self):
    response = self.client.get(self.entry.get_absolute_url())
    self.assertEqual(response.status_code, 200)

  def test_title_in_entry(self):
    response = self.client.get(self.entry.get_absolute_url())
    self.assertContains(response, self.entry.title)

  def test_body_in_entry(self):
    response = self.client.get(self.entry.get_absolute_url())
    self.assertContains(response, self.entry.body)

  def test_comment_name_in_entry(self):
    response = self.client.get(self.entry.get_absolute_url())
    self.assertContains(response, self.comment.name)

  def test_comment_body_in_entry(self):
    response = self.client.get(self.entry.get_absolute_url())
    self.assertContains(response, self.comment.body)

class CommentModelTest(TestCase):

  def test_string_representation(self):
    comment = Comment(body='My comment body')
    self.assertEqual(str(comment), 'My comment body')

class CommentFormTest(TestCase):

  def setUp(self):
    user = get_user_model().objects.create(username='some_user')
    self.entry = Entry.objects.create(author=user, title='My entry title')

  def test_init(self):
    CommentForm(entry=self.entry)

  def test_init_without_entry(self):
    with self.assertRaises(KeyError):
      CommentForm()
