from django.urls import path
from agent import views

urlpatterns = [
    path('entries/', views.EntryList.as_view()),
    path('entries/<int:pk>/', views.EntryDetail.as_view())
]
