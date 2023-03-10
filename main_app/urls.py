from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('verbiages/', views.VerbiageList.as_view(), name='verbiages_index'),
    path('verbiages/<int:verbiage_id>/', views.verbiages_detail, name="detail"),
    path('verbiages/create/', views.VerbiageCreate.as_view(), name='verbiages_create'),
    path('verbiages/<int:pk>/update/', views.VerbiageUpdate.as_view(), name='verbiages_update'),
    path('verbiages/<int:pk>/delete/', views.VerbiageDelete.as_view(), name='verbiages_delete'),
    path('verbiages/<int:verbiage_id>/add_etymology/', views.add_etymology, name="add_etymology")
]
