from django.urls import path
from .views import fun_view_test,Cls_view_Test

urlpatterns = [
    path("test_fun",fun_view_test),
    path("test_cls",Cls_view_Test.as_view()),
]
