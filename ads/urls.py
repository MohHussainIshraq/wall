from django.urls import path

from . import views

urlpatterns = [
    path('list', views.AdsListView.as_view(), name=''),
    path('create', views.AdCreateView.as_view(), name=''),
    path('detail/<int:pk>', views.AdDetailView.as_view(), name=''),
    path('search/', views.AdSearchView.as_view()),
]
