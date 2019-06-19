from django.test import TestCase
from myapp.models import Page
# These are tests that allow the server to be tested and ensure it is functioning as expected.

class pageTests(TestCase):

    def setUp(self):
        Page.objects.create(title="TestPage" content="Testing is fun!")
    
    def test_MakePage(self):
        TestPage = Page.object.get(title="TestPage")
        self.assertEqual(TestPage.content(), 'Testing is fun!')