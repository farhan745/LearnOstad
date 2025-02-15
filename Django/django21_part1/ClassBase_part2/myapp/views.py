from django.shortcuts import render,HttpResponse
from django.views import View
# Create your views here.
class MyClassView1(View):
    def get(self,request):
        return HttpResponse("<h1>Hello Class View</h1>")
class MyClassView2(View):
    def get(self,request):
        return HttpResponse("<h1>Class Based View</h1>")
class MyClassView3(View):
    name = 'Rahul'
    def get(self,request):
        return HttpResponse(f"<h1>Hello {self.name}</h1>")
    
class HomeClassView(View):
    def get(self,request):
        return render(request, 'school/home.html', {'name':'John Doe'})
    
class AboutClassView(View):
   def get(self,request): 
    context = {"msg": 'About Class View'}
    return render(request,'school/about.html', context)
    
class NewsClassView(View):
    template_name = ''
    def get(self,request):
        context = {"info": 'Welcome to News Channel'}
        return render(request,self.template_name, context)
    
    
    
class ContactClassView(View):
    def get(self,request):
        form = ContactForm()
        return render(request,'school/contact',{'form':form})
    def post(self,request):
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            return HttpResponse()
        else:
            return render(request,'school/contact',{'form':form})
