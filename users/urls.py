from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),

    path('', views.profiles, name="profiles"),
    path('profile/<str:pk>/', views.profile, name="profile"),
    path('account/' , views.account , name="account"),
    path('edit-account/', views.editAccount, name="edit-account"),
    path('add-skill/', views.addSkill, name="add-skill"),
    path('edit-skill/<str:pk>/', views.editSkill, name="edit-skill"),
    path('delete-skill/<str:pk>/', views.deleteSkill, name="delete-skill"),
]

