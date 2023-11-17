from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path("",views.main),
    path("<int:year>/",views.main),
    path("<int:year>/<str:team>/",views.detail,name='detail'),
    #추가한 코드
    #path("<int:year>/random/",views.randomExhibition, name = 'random'),
    path("random/<int:year>/",views.randomExhibition, name = 'random'),
]
