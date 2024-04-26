from django.urls import path
from . import views

urlpatterns=[
    path('',views.function,name="index"),
    path('submitquery/', views.submitquery1, name='submitquery'),
]