from django.urls import path
from . import views

urlpatterns=[
    path('sup/', views.SignUpView.as_view(), name='signup_url'),
    path('sin/', views.SignInView.as_view(), name='signin_url'),
    path('sout/', views.SignOutView.as_view(), name='signout_url')
]