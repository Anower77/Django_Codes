from django.shortcuts import render, redirect
# from .forms import AuthorForm  # Ensure your form is imported
from . import forms

def add_author(request):
    if request.method == 'POST':
        author_form = forms.AuthorForm(request.POST)
        if author_form.is_valid():
            author_form.save()
            return redirect('add_author')
    
    else:
        author_form = forms.AuthorForm()
    # author_form = AuthorForm()
    return render(request, 'add_author.html', {'form': author_form})
