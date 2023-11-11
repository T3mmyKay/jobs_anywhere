from django.shortcuts import render
from uploadapp.forms import UploadForm, UploadFileForm


# Create your views here.

def upload_image(request):
    form = UploadForm()
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            saved_object = form.instance
            return render(request, 'uploadapp/add_image.html', context={'form': form, 'saved_object': saved_object})

    return render(request, 'uploadapp/add_image.html', context={'form': form})


def upload_file(request):
    form = UploadFileForm()
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            saved_object = form.instance
            return render(request, 'uploadapp/add_file.html', context={'form': form, 'saved_object': saved_object})

    return render(request, 'uploadapp/add_file.html', context={'form': form})
