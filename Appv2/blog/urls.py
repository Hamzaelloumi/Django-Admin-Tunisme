from django.urls import path
from . import views
""" import the file urls and views.home the function in view """
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),

    path('create/', views.create, name='create' ),
    path('add_responsable/', views.add_responsable, name='add_responsable' ),
    path('delete/<id>/', views.delete, name='delete' ),
    path('edit/<id>/', views.edit, name='edit' ),
    path('update/<id>/', views.update, name='update' ),




    path('clinique/', views.clinique, name='clinique-home' ),
    path('create_clinique/', views.create_clinique, name='create_clinique' ),
    path('add_clinique/', views.add_clinique, name='add_clinique' ),

    path('delete_clinique/<id>/', views.delete_clinique, name='delete_clinique' ),
    path('edit_clinique/<id>/', views.edit_clinique, name='edit_clinique' ),
    path('update_clinique/<id>/', views.update_clinique, name='update_clinique' ),



    path('sanatorium/', views.sanatorium, name='sanatorium-home' ),
    path('create_sanatorium/', views.create_sanatorium, name='create_sanatorium' ),
    path('add_sanatorium/', views.add_sanatorium, name='add_sanatorium' ),

    path('delete_sanatorium/<id>/', views.delete_sanatorium, name='delete_sanatorium' ),
    path('edit_sanatorium/<id>/', views.edit_sanatorium, name='edit_sanatorium' ),
    path('update_sanatorium/<id>/', views.update_sanatorium, name='update_sanatorium' ),


    path('hote/', views.hote, name='hote-home' ),
    path('create_hote/', views.create_hote, name='create_hote' ),
    path('add_hote/', views.add_hote, name='add_hote' ),

    path('delete_hote/<id>/', views.delete_hote, name='delete_hote' ),
    path('edit_hote/<id>/', views.edit_hote, name='edit_hote' ),
    path('update_hote/<id>/', views.update_hote, name='update_hote' ),

]
