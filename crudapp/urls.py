from django.urls import path
from . import views

urlpatterns=[
    path('', views.TanishqView.as_view(), name='form_url'),
    path('tv/', views.OrderDisplay.as_view(), name='display_url'),
    path('edit/<int:pk>/', views.EditOrder.as_view(), name='edit_url'),
    path('del/<int:pk>/', views.DeleteOrder.as_view(), name='del_url'),
]