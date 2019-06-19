from django.contrib import admin


from .models import Page, UserFileUpload

admin.site.register(Page)                   # Models are defined here, this makes them useable.

admin.site.register(UserFileUpload)