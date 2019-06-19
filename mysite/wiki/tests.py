from django.test import TestCase
from myapp.models import Page
# Create your tests here.

class pageTests(TestCase):

    def setUp(self):
        Page.objects.create(title="TestPage" content="Testing is fun!")
    
    def test_MakePage(self):
        TestPage = Page.object.get(title="TestPage")
        self.assertEqual(TestPage.content(), 'Testing is fun!')