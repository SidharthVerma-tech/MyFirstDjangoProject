from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('sidharth',views.sidharth, name="sidharth"),
    path('shivanshu',views.shivanshu, name="shivanhsu"),
    path('<str:name>', views.greet, name="greet"),
]