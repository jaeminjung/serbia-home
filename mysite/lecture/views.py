from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .models import UploadFileModel
# Create your views here.

def lecture_notes(request):
    notes = UploadFileModel.objects.all().order_by('-uploaded_date')
    # print(notes[0])
    return render(request, 'lecture/lecture_notes.html', {'notes':notes})

def lecture_uploaded(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lecture_notes')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})