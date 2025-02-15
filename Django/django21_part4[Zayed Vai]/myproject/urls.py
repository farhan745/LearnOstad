from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def home(request):
    return JsonResponse(
        {"message": "Home", "Name": "Goku", "Age": 21, "status": "success"}
    )


@csrf_exempt
def method(request):
    print(f"Method: {request.method}")
    print(f"Headers: {request.headers}\n")
    print(f"Body: {request.body}\n")
    print(f"Params: {request.GET}")
    x = request.method
    if x == "GET":
        return JsonResponse(
            {"Method": x, "message": "Reading Data", "status": "success"}
        )
    elif x == "POST":
       if request.headers.get("Content-Type") == "application/json":
        data = json.loads(request.body)
        print(data)
       else:
        data = request.POST.dict()
        files=request.FILES
        print(data)
        print(files)
       return JsonResponse(
            {"Method": x, "message": "Creating Data", "status": "success"}
        )
    elif x in ["PUT", "PATCH"]:
        return JsonResponse(
            {"Method": x, "message": "Updating Data", "status": "success"}
        )
    elif x == "DELETE":
        return JsonResponse(
            {"Method": x, "message": "Deleting Data", "status": "success"}
        )
    return HttpResponse("Hello World")

from sampleapp.views import form_view,TaskCreateView,TaskCreateReadyMadeView

urlpatterns = [
    
            path("admin/", admin.site.urls),
            path("", home),
            path("method/", method),
            # path("form-view/", form_view),
             path('form-view/', TaskCreateView.as_view())
             #path('form-view/', TaskCreateReadyMadeView.as_view())

               ]
