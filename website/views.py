from django.shortcuts import render

# Create your views here.
def get_list(request):
    return(request, 'website/get_list.html')