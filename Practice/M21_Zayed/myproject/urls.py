from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from sampleapp.views import form_view,TaskCreateView,TaskCreateReadymadeView


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
    if x == "POST":
        data = request.POST.dict()
        files = request.FILES
        print(f"\nData: {data}")
        print("Files ",files)
        return JsonResponse(
            {"Method": x, "message": "Creating Data", "status": "success"}
        )
    if x in ["PUT", "PATCH"]:
        return JsonResponse(
            {"Method": x, "message": "Updating Data", "status": "success"}
        )
    if x == "DELETE":
        return JsonResponse(
            {"Method": x, "message": "Deleting Data", "status": "success"}
        )
    return HttpResponse("Hello World")


urlpatterns = [
    
            path("admin/", admin.site.urls),
            path("", home),
            path("method/", method),
            # path("form-view/", form_view),
            #path("form-view/", TaskCreateView.as_view()),
            path("form-view/", TaskCreateReadymadeView.as_view()),

               ]
