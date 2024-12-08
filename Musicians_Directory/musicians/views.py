# from django.shortcuts import render, redirect
# from . import models

# def home(request):
#     musician = models.Musician.objects.all()
#     return render(request, 'home.html', {'data' : musician})



from django.shortcuts import render, redirect, get_object_or_404
from .models import Musician, Album
from .forms import MusicianForm, AlbumForm

def home(request):
    musician = Musician.objects.all()
    return render(request, 'home.html', {'data': musician})




def add_musician(request):
    if request.method == 'POST':
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = MusicianForm()
    return render(request, 'add_musician.html', {'form': form})

def edit_musician(request, pk):
    # post = models.Post.objects.get(pk=id)
    musician = get_object_or_404(Musician, pk=pk)
    if request.method == 'POST':
        form = MusicianForm(request.POST, instance=musician)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = MusicianForm(instance=musician)
    return render(request, 'edit_musician.html', {'form': form})





def delete_musician(request, pk):
    musician = get_object_or_404(Musician, pk=pk)
    musician.delete()
    return redirect('homepage')
