from django.shortcuts import render

# Create your views here.
from .models import Category

def vw_CategoryList(request):
    qs_AllCategories = Category.objects.all() #filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    return render(request, template_name, {'all_ctgs': qs_AllCategories})
    #return render(request, template_name, {})
