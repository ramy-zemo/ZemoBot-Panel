from django.shortcuts import render

# Create your views here.


def error_400(request, *args, **kwargs):
    return render(request, "invalid_request_type.html")
