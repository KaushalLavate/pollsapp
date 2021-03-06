from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('<int:question_id>/',views.detail, name='details'),
    path('<int:question_id>/results/',views.result,name='results'),
    path('<int:question_id>/votes/',views.vote,name='vote')
]