from django.urls import path, re_path

from . import views

app_name = 'traitement'


urlpatterns = [

    path('traitement/', views.TraitementView.as_view()),
    path('doctors/', views.DoctorsViewSet.as_view()),
    path('usertraitement/', views.UserTraitementViewSet.as_view()),
    re_path(r'^trait/(?P<pk>[0-9]+)$',views.get_delete_update.as_view(),name='get_delete_update '),

    ]
