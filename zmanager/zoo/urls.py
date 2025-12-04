from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.dashboard, name='dashboard'),
]

urlpatterns += [
    path('animal/add/', views.add_animal, name='add_animal'),
    path('animal/edit/<int:id>/', views.edit_animal, name='edit_animal'),
    path('animal/delete/<int:id>/', views.delete_animal, name='delete_animal'),
]
