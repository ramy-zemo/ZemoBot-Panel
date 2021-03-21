from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login', redirect_field_name="")
def contact_view(request, *args, **kwargs):
    my_context = {
        "my_text": 11,
        "my_number": 12345,
        "my_list": [1, 2, 3, 4]
    }
    return render(request, "contact.html", my_context)


@login_required(login_url='/login', redirect_field_name="")
def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})