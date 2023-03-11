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
    path('verbiages/<int:verbiage_id>/add_etymology/', views.add_etymology, name="add_etymology"),
    path('verbiages/<int:verbiage_id>/assoc_fact/<int:fact_id>/', views.assoc_fact, name="assoc_fact"),
    path('verbiages/<int:verbaige_id>/unassoc_fact/<int:fact_id>/', views.unassoc_fact, name="unassoc_fact"),
    path('facts/', views.FactList.as_view(), name='facts_index'),
    path('facts/<int:pk>/', views.FactDetail.as_view(), name='facts_detail'),
    path('facts/create/', views.FactCreate.as_view(), name='facts_create'),
    path('facts/<int:pk>/update/', views.FactUpdate.as_view(), name='facts_update'),
    path('facts/<int:pk>/delete/', views.FactDelete.as_view(), name='facts_delete')
]
