from django.views import generic
from .models import Page, UserFileUpload
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UploadFileForm
from django.db.models import F
import logging

logger = logging.getLogger(__name__) # Allows us to keep a log of which pages are being requested. 
# Views are the like child clasess to the models, they build off the page classes and create the data structures that make up specific pages.

class IndexView(generic.ListView):
    template_name = 'wiki/index.html'
    context_object_name = 'pages'
    def get_queryset(self):
        return Page.objects.all().order_by('title')
    
    
class DetailView(generic.DetailView):
    model = Page
    template_name = 'wiki/detail.html'

def view_page(request, pk):
    try:
        page = Page.objects.get(pk=pk)
        page.counter = F('counter') + 1
        page.save()
        page.refresh_from_db()
        return render(request, 'wiki/detail.html', {'page': page})
    except Page.DoesNotExist:
        return render(request, 'wiki/create_page.html', {'page_name': pk})

@login_required(login_url='wiki:login') # Authenticates the page, people cannot access that page without being logged in.
def edit_page(request, pk):
    try:
        page= Page.objects.get(pk=pk)
        content = page.content
    except Page.DoesNotExist:
        content=''
    return render(request, 'wiki/edit_page.html',{ 'page_name':pk, 'content':content},)

@login_required(login_url='wiki:login')
def save_page(request, pk):                                  # This page is vulnerable to XSS attacks, alongside view page. If this were on a larger scale, it would be something i would patch out by not allowing JavaScript to be saved as JavaScript. It would be saved as text.
    content = request.POST["content"]
    try:
        page = Page.objects.get(pk=pk)
        page.content = content
    except Page.DoesNotExist:
        page = Page(title=pk, content=content)
    if 'Save' in request.POST:
        page.save()
    return redirect(page)

@login_required(login_url='wiki:login')                          # No proofing here, technically a security risk, but that could be handled by having the appropriate software in the server itself to check files.
def upload_file(request):
    context = {}
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = UploadFileForm()
    context['form'] = form
    context['files'] = UserFileUpload.objects.all().order_by('upload')
    return render(request, 'wiki/upload.html', context)
