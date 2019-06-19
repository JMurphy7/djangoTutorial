from django.forms import ModelForm
from .models import UserFileUpload
class UploadFileForm(ModelForm):
    class Meta:
        model = UserFileUpload                # Forms are what accept user files, in this instance, there is a single form which accepts input
        fields = ['upload' ]