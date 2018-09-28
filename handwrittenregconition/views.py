from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import platform
from .forms import UploadFileForm
from .process_uploaded_file import handle_uploaded_file
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


def test_function(number):
    x = number * 2
    return x

@csrf_exempt
def index(request):
    my_number = test_function(3)

    if request.method == 'POST' :
        # form = UploadFileForm(request.POST, request.FILES)
        # if form.is_valid():
        #     my_number = handle_uploaded_file(request.FILES['file'])

        my_number = handle_uploaded_file(7)

    return JsonResponse({'number': my_number})
    # return HttpResponse("Hello world ! Python version is " + platform.python_version() + ". Your number is " + str(my_number) )

