from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from account.forms import EntryForm, EntryModelForm

from account.models import Developer


def home_view(request):
    #get data
    #define format
    #render output
    devs1 = Developer.objects.all()
    context = {
        "devs" : devs1
    }
    return render(request, "index.html", context)

@login_required
def entry_view(request):
    
    if request.method == "POST":
        form = EntryForm(request.POST)
        if form.is_valid():
            print("ok")
            fn = form.cleaned_data["firstname"]
            mn = form.cleaned_data["middlename"]
            bd = form.cleaned_data["birthdate"]
            # print(fn)
            dev = Developer(
                firstname = fn,
                middlename=mn,
                birthdate = bd
            )
            dev.save()
        else:
            print("not ok")
    else:
        form = EntryForm()
    context = {
        "form" : form
    }
    return render(request, "entry_view.html", context)


def model_entry_view(request):
    if request.method == "POST":
        form = EntryModelForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            print("not ok")
    else:
        form = EntryForm()
    context = {
        "form" : form
    }
    return render(request, "entry_view.html", context)

def htmxget(request):
    context = {
        "name" : "ISMD"
    }
    return render(request, "walalang.html",  context)