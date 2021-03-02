from django.shortcuts import render 
from .forms import HeadwordForm 

def head_word_view(request):
	form = HeadwordForm()
	return render(request, "dict.html" , {"form":form})
