from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def talha(request):
    return HttpResponse("Hello, Talha. You're at the talha's index.")
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('talha/', talha),
    path('<int:question_id>/', detail),
    path('<int:question_id>/results/', results),
]
