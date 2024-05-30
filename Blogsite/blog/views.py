from django.shortcuts import render
from .models import Blog,Category

# Create your views here.

def home(request):
    blogs  = Blog.objects.all()
    category = Category.objects.all()
    return render(request,'index.html',{'blogs':blogs})
