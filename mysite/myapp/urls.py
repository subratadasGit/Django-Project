
from django.urls import path
from . import views

urlpatterns = [

    path('all_app',views.all_app,name='myapp'),
]