from django.db import models
from django.urls import reverse

# Models are the classes that make up the webpages in the server. 

class Page(models.Model):
    title = models.CharField(max_length=64, primary_key=True)
    content = models.TextField()
    counter = models.IntegerField(default = 1)
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('wiki:detail', args=[self.title])      # Sends the user to the page that they have requested, and retrieves the content depending on the site asked for.


class UserFileUpload(models.Model):
    upload = models.FileField(upload_to='uploads/')           # Uploads are stored as a class

    def __str__(self):
        return self.upload.name
