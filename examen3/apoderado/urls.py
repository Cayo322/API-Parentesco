from django.urls import path

from . import views

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('apoderado',views.ApoderadoView.as_view(),name='apoderado'),
    path('apoderado/<int:apoderado_id>',views.ApoderadoDetailView.as_view())
]
