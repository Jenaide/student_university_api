from django.urls import path
from api import views

urlpatterns = [
    path('', views.student_list),
    path('student/<int:id>', views.student_details)
]