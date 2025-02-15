from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import ContactForm
# Create your views here.
class MyView(View):
    name = None
    def get(self, request):
        return render(request,'school/home.html')

class aboutfun(View):
    def get(self, request):
        context = {"msg": "about this course"}
        return render(request,'school/about.html',context)
    

class ContactClassView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'school/contact.html', {'form': form})
    
    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            # save data to database
            print(name)
            return HttpResponse('Submitted')
        else:
            return render(request, 'school/contact.html', {'form': form})