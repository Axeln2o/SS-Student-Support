from django.urls import path

from home import views

urlpatterns = [
    path('first_page/', views.index, name='index'),
    path('details_students/', views.show_details_students, name='student_details'),
    path('details_phones/', views.show_details_phones, name='phones_details'),
    path('details_professors', views.show_details_professors, name='professors_details'),
    path('', views.HomeTemplateView.as_view(), name='home')
]
