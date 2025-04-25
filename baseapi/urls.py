
from django.urls import path,include
from .views import *
from . import views

urlpatterns = [
    # path('student',StudentAPI.as_view()),
    # path('student/<int:id>/',StudentAPI.as_view()),
    # path('register/',ResgisterUser.as_view()),
    # path('', views.home, name='home'),
    # path('post', views.post_data, name='post_data'),
    # path('update-student/<int:id>/', views.update_student, name='update_student'),
    # path('delete/<int:id>/', views.delete_student, name='delete_student'),
    # path('get_book', views.get_book, name='get_book'),
    path('StudentGeneric', StudentGeneric.as_view(), name='StudentGeneric'),
    path('StudentGeneric1', StudentGeneric1.as_view(), name='StudentGeneric1'),
    path('pdf', GeneratetoPdf.as_view(), name='GeneratetoPdf'),
]
