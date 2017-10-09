from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django import forms
from collection.models import Social

def ssn_test(ssn):
    # function to check if an SSN follows SSA rules
    ssn = ssn.value
    ssn = ssn.strip().replace("-","").replace(" ", "")
    if len(ssn) == 9 and ssn.isdigit():
        out_msg = "So far so good! This SSN has exactly 9 digits"
    elif len(ssn) != 9:
        out_msg = "This SSN isn't the right length. It's {0} characters".format(len(ssn))
    else:
        out_msg = "The length is correct, but something else is wrong. You entered {0} - there may be non-numeric characters".format(ssn)
    return out_msg


# Create your views here.
def index(request):
    # defining a variable
    #number = 6 + 9
    #new views
    return render(request, 'index.html', {'number': ssn_test("123456789"),})


class MyForm(forms.Form):
    testnum = forms.CharField(max_length=50)

def formview(request):
    #if the form has been submitted
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            testnum = form['testnum']
            test_results = ssn_test(testnum)
        return render(request, 'ssnapp/out.html', {'results': test_results})
    else:
        #unbound form
        form = MyForm()
    # pass variables
    return render(request, 'formtemplate.html', {'form': form})
