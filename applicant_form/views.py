from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from . import models
from .MyForms import ApplicantForm
from django.core.exceptions import ValidationError

def index(request):
    return HttpResponse("Hello, appliants. You can complete this form to apply.")

#def apply_form(request):
#    if request.method == "GET":
#        form = ApplicantForm()
#        return render(request, "add_applicant_form.html", {"form": form})
#    else:
#        form = ApplicantForm(request.POST)
#        if form.is_valid():  # 进行数据校验
#            return HttpResponse(
#                'ok'
#            )
#        else:
#            print(form.errors)    # 打印错误信息
#            clean_errors = form.errors.get("__all__")
#            print(222, clean_errors)
#        return render(request, "add_applicant_form.html", {"form": form, "clean_errors": clean_errors})

def apply_form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ApplicantForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ApplicantForm()

    return render(request, 'add_applicant_form.html', {'form': form})